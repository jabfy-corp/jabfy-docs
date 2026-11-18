# Vie privée

| Statut                                                     | Suivi par | Dernière mise à jour |
| ---------------------------------------------------------- | --------- | -------------------- |
| Première version : principes appliqués, preuves à produire | Simeon    | 27/10/2026           |

## Le problème

Un assistant domestique entend tout ce qui se dit dans la maison, connaît les habitudes de ses occupants et pilote leurs serrures. Jabfy promet qu'**aucune donnée ne quitte la maison**. Il faut le garantir techniquement, le démontrer, et décider ce que l'on conserve sur place : transcriptions, journal d'audit, état des appareils.

## Situation actuelle

Ce qui est déjà en place :

* **tout le traitement est local** : transcription (faster-whisper), raisonnement (modèle servi par Ollama ou llama.cpp), synthèse (Kokoro) ;
* **le journal d'audit** de jabfy-bus trace chaque décision, et sa chaîne de hash rend toute modification détectable ;
* **l'API du bus est en lecture seule**, et n'accepte que les origines navigateur autorisées.

Ce qui manque ou pose problème :

* l'interface web de jabfy-voice écoute sur tout le réseau local, sans authentification, et expose la conversation ;
* aucune durée de conservation n'est définie pour le journal d'audit ni pour l'historique des conversations ;
* l'absence de trafic sortant n'a pas encore été démontrée par une capture réseau.

## Les solutions existantes

* **Assistants cloud (Amazon Alexa, Google Assistant)** — reconnaissance et raisonnement sur les serveurs du fournisseur. Depuis le 28 mars 2025, Amazon a supprimé l'option qui traitait localement la voix sur certains Echo : toutes les requêtes partent désormais dans son cloud, pour alimenter Alexa+.
* **Home Assistant Assist** — assistant domotique local et open source : reconnaissance, intentions et synthèse peuvent tourner entièrement à la maison.
* **Approche Jabfy** — tout en local, plus une vérification déterministe de chaque action et un journal d'audit infalsifiable.

## Comparatif

| Approche                               | 100 % local                                   | Latence                                                      | Qualité en français              | Ressources locales                 | Licence                                                   | Données conservées                    |
| -------------------------------------- | --------------------------------------------- | ------------------------------------------------------------ | -------------------------------- | ---------------------------------- | --------------------------------------------------------- | ------------------------------------- |
| Alexa / Google Assistant               | **Non** : voix et texte traités dans le cloud | Faible (réseau)                                              | Très bonne                       | Minimes                            | Propriétaire                                              | Chez le fournisseur, selon ses règles |
| Home Assistant Assist (pipeline local) | Oui                                           | Faible à moyenne                                             | Bonne, selon les modèles choisis | Moyennes                           | Apache 2.0                                                | Sur place                             |
| Jabfy                                  | Oui                                           | Mesurée : voir [Performance](../../performance/performance/) | Bonne, selon les modèles choisis | Moyennes : modèle de langage local | À décider (voir [Licences](../../protection/licences.md)) | Sur place, dans le journal d'audit    |

## Choix retenu

Jabfy applique le principe de **minimisation par conception** :

1. **Aucun traitement dans le cloud.** Le seul accès à Internet est le téléchargement initial des modèles.
2. **Rien n'est enregistré par défaut** en dehors de ce qui est utile à la sécurité : l'audit des commandes.
3. **Toute action est vérifiée et tracée**, ce qui permet à l'utilisateur de savoir ce qui a été fait chez lui, et pourquoi.

Actions à mener :

* [ ] Démontrer l'absence de trafic sortant : capture réseau pendant un scénario complet de jabfy-simulation.
* [ ] Limiter l'interface web de jabfy-voice à la machine locale (`127.0.0.1`).
* [ ] Définir et implémenter une durée de conservation pour l'audit et les conversations.
* [ ] Documenter pour l'utilisateur ce qui est conservé, où, et comment l'effacer : voir [Protection › RGPD](../../protection/rgpd.md).

## Avancées récentes

* **Amazon a supprimé le traitement local d'Alexa** (28 mars 2025) pour ses fonctions d'IA générative : la tendance des grands acteurs va vers _plus_ de cloud, ce qui renforce la différence de Jabfy.
* **Les modèles locaux ont rattrapé l'usage domestique** : transcription, petits modèles de langage et synthèse tiennent aujourd'hui sur une machine sans GPU (voir les fiches [STT](stt.md), [LLM local](llm-local.md) et [TTS](tts.md)).
* **Le cadre européen** encadre spécifiquement les assistants vocaux : les lignes directrices 02/2021 du CEPD rappellent la minimisation des données et le consentement pour l'enregistrement de la voix.

## Sources

* [TechCrunch — Amazon Echo enverra toutes les requêtes vocales dans le cloud à partir du 28 mars 2025](https://techcrunch.com/2025/03/15/amazons-echo-will-send-all-voice-recordings-to-the-cloud-starting-march-28)
* [The Register — Amazon supprime le traitement local d'Alexa](https://www.theregister.com/2025/03/17/amazon_kills_on_device_alexa/)
* [CEPD — Lignes directrices 02/2021 sur les assistants vocaux virtuels](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-022021-virtual-voice-assistants_en)
* [Home Assistant — Assist et approche du wake word local](https://home-assistant.io/voice_control/about_wake_word)
