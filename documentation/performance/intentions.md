# Compréhension des intentions

| Suivi par | Valeur de départ | Cible | Dernière mesure |
|---|---|---|---|
| Joan | 8/10 (Llama 3.2 3B) | 10/10 sur le jeu de base, ≥ 95 % sur le jeu étendu | 27/10/2026 |

## Définition

Part des consignes pour lesquelles le modèle propose **la bonne action** : tous les changements attendus, sans changement contraire, ou **aucun changement** quand la demande n'en appelle pas. Deux mesures associées :

- **JSON valide** : la réponse est exploitable par jabfy-core (même parseur et même règle de vérification) ;
- **latence** : temps de réponse du modèle, qui alimente l'étape `t_llm` de la [latence de bout en bout](latence.md).

## Protocole de mesure

- Script : [`benchmarks/bench_llm.py`](https://github.com/jabfy-corp/jabfy-docs/blob/main/benchmarks/bench_llm.py). Il reprend le prompt système, le message, le parseur et le vérificateur de jabfy-core (`main` `a3b9aa7`).
- **10 consignes en français**, chacune avec un état de départ et le résultat attendu : ordres directs (« Allume la lumière de la cuisine »), intentions implicites (« J'ai froid », « Je pars de la maison »), demandes multiples, et une question hors sujet (« Quelle heure est-il ? »).
- Température 0,2, graine fixe, une exécution par consigne après un appel de chauffe.
- Deux modes : le prompt seul, comme jabfy-core aujourd'hui, et les **sorties structurées** d'Ollama (schéma JSON listant les appareils autorisés).

## Résultats

Machine : i7-13700HX, RTX 5060 Laptop 8 Go, 23 Go de RAM, Ollama 0.17.7, modèles quantifiés en Q4_K_M.

| Modèle | Mode | Matériel | Bonne action | JSON valide | Latence médiane | Débit |
|---|---|---|---|---|---|---|
| Llama 3.2 3B | Prompt seul | GPU | 8/10 | 10/10 | 0,33 s | 105 tokens/s |
| Llama 3.2 3B | Sorties structurées | GPU | 8/10 | 10/10 | 0,49 s | 138 tokens/s |
| Llama 3.2 3B | Prompt seul | **CPU seul** | 8/10 | 10/10 | 1,13 s | 28 tokens/s |
| Ministral 3 8B | Prompt seul | GPU | **10/10** | 10/10 | 1,08 s | 41 tokens/s |
| Ministral 3 8B | Sorties structurées | GPU | **10/10** | 10/10 | 0,95 s | 42 tokens/s |
| Ministral 3 8B | Prompt seul | **CPU seul** | **10/10** | 10/10 | 3,55 s | 12 tokens/s |

Échecs de Llama 3.2 :

| Consigne | Attendu | Proposé |
|---|---|---|
| « Je pars de la maison. » | verrouiller, activer l'alarme | verrouiller, **allumer** le couloir et la cuisine |
| « Quelle heure est-il ? » | aucune action | **éteindre la lumière de la cuisine** |

## Analyse

- **La taille du modèle fait la compréhension** : 8 milliards de paramètres réussissent les intentions implicites et les questions hors sujet, 3 milliards non.
- **Les sorties structurées ne changent pas la compréhension**, mais garantissent un JSON conforme et sans appareil inventé, pour un coût en latence négligeable. Elles sont à activer dans jabfy-core.
- **Le vérificateur doit protéger contre le modèle** : l'action non demandée de Llama 3.2 porte sur un appareil valide, avec une valeur valide, et passerait donc le vérificateur actuel de jabfy-core. Seules des règles de risque et de contexte, celles de jabfy-guard, peuvent l'arrêter.
- **Limite de la mesure** : 10 consignes, une seule exécution chacune. C'est une première tendance, pas un résultat statistique.

## Prochaines étapes

| Date | Action | Statut |
|---|---|---|
| À faire | Étendre le jeu à 50 consignes, dont des formulations orales issues de la transcription | — |
| À faire | Mesurer Qwen2.5 1.5B (modèle de la V0.0.1), Qwen3.5 4B et Gemma 4 E4B | — |
| À faire | Mesurer sur la machine cible, une fois celle-ci définie | — |
