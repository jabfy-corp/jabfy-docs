# LLM local

| Statut                                                            | Suivi par | Dernière mise à jour |
| ----------------------------------------------------------------- | --------- | -------------------- |
| Première version : moteur confirmé, modèle à trancher sur mesures | Joan      | 27/10/2026           |

## Le problème

Transformer une demande en français et l'état des appareils en une **proposition d'action JSON valide**, sur une machine domestique, en quelques secondes au plus. Le modèle ne pilote jamais rien lui-même : il propose, et une vérification déterministe décide. Trois exigences en découlent :

* **comprendre l'intention**, y compris implicite (« j'ai froid » → chauffage) ;
* **ne rien inventer** : pas d'action quand la demande n'en appelle aucune ;
* **produire un JSON exploitable à chaque fois**.

## Situation actuelle

* [jabfy-core](../../composants/composants.md) passe par une **API compatible OpenAI** : il fonctionne avec llama.cpp comme avec Ollama, et extrait le JSON de la réponse avant vérification.
* [jabfy-deploy](../../composants/composants.md) fournit **Ollama**, avec `qwen2.5:1.5b` par défaut.
* [jabfy-voice](../../composants/composants.md) utilise `llama3.2` via Ollama.
* Limite connue : les modèles « raisonneurs » qui répondent dans un champ de réflexion séparé laissent la réponse vide, et la proposition est rejetée.

## Les solutions existantes

**Moteurs d'inférence**

* **Ollama** — installation simple, catalogue de modèles, API compatible OpenAI, et sorties structurées par schéma JSON depuis décembre 2024.
* **llama.cpp** — le moteur sous-jacent d'Ollama, utilisable directement ; le plus de contrôle, avec des grammaires pour contraindre la sortie.

**Petits modèles ouverts** (moins de 10 milliards de paramètres)

* **Qwen2.5 1.5B** (Alibaba) — le modèle par défaut de la V0.0.1.
* **Llama 3.2 3B** (Meta).
* **Ministral 3 8B** (Mistral AI, décembre 2025) — conçu pour l'embarqué, multilingue dont le français.
* **Qwen3.5 4B et 9B** (mars 2026), **Gemma 4 E4B** (Google, avril 2026) — génération récente, avec appel de fonctions natif.

## Comparatif

Mesures Jabfy du 27/10/2026, avec le prompt et le parseur de jabfy-core, sur 10 consignes en français (voir [Performance › Intentions](../../performance/intentions.md)). Machine de développement : i7-13700HX, RTX 5060 8 Go, Ollama 0.17.7, quantification Q4\_K\_M.

| Modèle                   | 100 % local | Latence médiane GPU | Latence médiane CPU seul | Bonne action | JSON valide | Taille | Licence                               |
| ------------------------ | ----------- | ------------------- | ------------------------ | ------------ | ----------- | ------ | ------------------------------------- |
| Llama 3.2 3B             | Oui         | 0,33 s              | 1,13 s                   | 8/10         | 10/10       | 2,0 Go | Llama 3.2 Community License (non OSI) |
| Ministral 3 8B           | Oui         | 1,08 s              | 3,55 s                   | **10/10**    | 10/10       | 6,0 Go | Apache 2.0                            |
| Qwen2.5 1.5B (V0.0.1)    | Oui         | À mesurer           | À mesurer                | À mesurer    | À mesurer   | \~1 Go | Apache 2.0                            |
| Qwen3.5 4B / Gemma 4 E4B | Oui         | À mesurer           | À mesurer                | À mesurer    | À mesurer   | \~3 Go | Apache 2.0                            |

Ce que montrent les mesures :

* **Le JSON n'est pas le problème** : 10/10 partout, même sans contrainte de schéma.
* **La compréhension, si.** Llama 3.2 rate « Je pars de la maison » (il verrouille, mais n'active pas l'alarme et allume des lumières) et, à « Quelle heure est-il ? », **éteint une lumière que personne n'a mentionnée**. Ministral 3 réussit les 10 cas.
* **Le prix de la qualité est la latence** : sans GPU, Ministral 3 met 3,5 s, contre 1,1 s pour Llama 3.2.

## Choix retenu

**Moteur : Ollama ou llama.cpp, derrière une API compatible OpenAI**, comme le fait déjà jabfy-core ([ADR-0003](../../architecture/adr/0003-modele-local.md)). Changer de moteur ou de modèle ne demande que de la configuration.

**Modèle : la décision n'est pas encore prise**, mais les mesures orientent vers un modèle d'environ 8 milliards de paramètres de type **Ministral 3 8B** :

* seul modèle testé à comprendre toutes les consignes, dont les intentions implicites et les questions hors sujet ;
* licence Apache 2.0, éditeur européen, français natif ;
* 3,5 s sur CPU reste acceptable pour une commande vocale, et descend à 1 s avec un GPU.

Avant de trancher, il faut mesurer **Qwen2.5 1.5B** (le modèle actuel de la V0.0.1), **Qwen3.5 4B** et **Gemma 4 E4B** sur un jeu de consignes plus large.

À appliquer quel que soit le modèle :

* **activer les sorties structurées** (schéma JSON listant les appareils autorisés) : elles n'améliorent pas la compréhension, mais garantissent un JSON valide et sans appareil inventé ;
* **ne pas compter sur le modèle pour la sécurité** : l'action non demandée de Llama 3.2 serait passée à travers le vérificateur actuel de jabfy-core, qui ne contrôle que les noms d'appareils. C'est le rôle de jabfy-guard (risques, politiques, refus par défaut).

Écartés : les grands modèles (plus de 20 milliards de paramètres), trop lourds pour une box domestique, et les modèles « raisonneurs » en mode réflexion, trop lents pour une commande courte et incompatibles avec le parseur actuel.

## Avancées récentes

* **Ministral 3** (décembre 2025, Mistral AI) : 3B, 8B et 14B sous Apache 2.0, pensés pour l'embarqué.
* **Qwen3.5** (mars 2026) : petits modèles de 0,8B à 9B sous Apache 2.0.
* **Gemma 4** (avril 2026) : passage de Google à la licence Apache 2.0, appel de fonctions et JSON structuré natifs.
* **Sorties structurées** (Ollama depuis décembre 2024, grammaires de llama.cpp) : la génération est contrainte token par token pour respecter un schéma JSON.
* **Modèles spécialisés domotique** (projet Home-LLM) : petits modèles affinés sur des commandes Home Assistant, pour le matériel le plus modeste.

## Sources

* [Ollama — sorties structurées](https://registry.ollama.ai/blog/structured-outputs)
* [llama.cpp — grammaires et schémas JSON](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md)
* [Mistral AI — Ministral 3 3B Instruct (fiche Hugging Face, Apache 2.0)](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-BF16)
* [Artificial Analysis — petits modèles Qwen3.5](https://artificialanalysis.ai/articles/qwen3-5-small-models)
* [Gemma 4 : tailles et licence Apache 2.0 (article tiers)](https://emelia.io/hub/gemma-4-open-source-guide)
* [Best local LLMs for Home Assistant 2026 (comparatif tiers)](https://www.promptquorum.com/smart-home/best-local-llm-models-smart-home)
* Scripts de mesure Jabfy : [`benchmarks/`](../../../benchmarks/)
