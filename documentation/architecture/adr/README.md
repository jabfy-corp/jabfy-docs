# Décisions d'architecture (ADR)

Un ADR (_Architecture Decision Record_) est une fiche courte qui consigne **une** décision : le contexte, les options étudiées, ce qui a été décidé et ce que ça implique. C'est le lien entre la [veille](../../veille/veille/) et l'architecture.

## Index

| #                                       | Décision                                                  | Statut                               | Veille liée                                                |
| --------------------------------------- | --------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------- |
| [0001](0001-consigner-les-decisions.md) | Consigner les décisions dans des ADR                      | Accepté                              | —                                                          |
| [0002](0002-fastapi.md)                 | FastAPI pour les API Python                               | Accepté                              | —                                                          |
| [0003](0003-modele-local.md)            | Modèle local via une API compatible OpenAI                | Accepté                              | [LLM local](../../veille/etudes/llm-local.md)              |
| [0004](0004-electron-react.md)          | Electron et React pour le client desktop                  | Accepté                              | —                                                          |
| [0005](0005-mqtt-zigbee2mqtt.md)        | MQTT et Zigbee2MQTT comme protocoles prioritaires         | Accepté                              | [Protocoles](../../veille/etudes/protocoles-domotiques.md) |
| [0006](0006-bus-et-guard-embarques.md)  | Bus et Guard embarqués comme bibliothèques dans la V0.0.1 | Accepté pour la V0.0.1, à réexaminer | —                                                          |
| [0007](0007-ia-propose-guard-decide.md) | L'IA propose, une vérification déterministe décide        | Accepté (principe fondateur)         | [LLM local](../../veille/etudes/llm-local.md)              |
| [0008](0008-faster-whisper.md)          | faster-whisper pour la reconnaissance vocale              | Accepté                              | [STT](../../veille/etudes/stt.md)                          |
| [0009](0009-kokoro-tts.md)              | Kokoro-82M pour la synthèse vocale                        | Accepté                              | [TTS](../../veille/etudes/tts.md)                          |
| [0010](0010-documentation-agregee.md)   | Un site de documentation unique, alimenté par chaque repo | Accepté                              | —                                                          |

Les ADR 0002 à 0009 ont été rédigés **a posteriori**, le 27/10/2026, à partir de décisions déjà appliquées dans le code : ils restent à relire par l'équipe.

## Décisions à venir

| Sujet                                                              | Pourquoi c'est urgent                                                           | Veille liée                                   |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------- |
| Où embarquer le bus : dans la simulation ou dans Core              | Deux branches divergentes à réconcilier avant la fusion de la V0.0.1 sur `main` | [Vue globale](../vue-globale.md)              |
| Contrat d'API de Core (`/act`, `/simulation/propose` ou `/prompt`) | Trois versions selon la branche                                                 | [Interfaces](../interfaces.md)                |
| Modèle de langage par défaut                                       | Les mesures montrent un écart net de compréhension entre 3B et 8B               | [LLM local](../../veille/etudes/llm-local.md) |
| Moteur de wake word                                                | Prérequis de la commande vocale                                                 | [Wake word](../../veille/etudes/wake-word.md) |
| Relier jabfy-voice (Python) et jabfy-tts (Rust)                    | Prérequis de la réponse vocale                                                  | [TTS](../../veille/etudes/tts.md)             |
| Politique de licence des repos                                     | Repos publics sans licence                                                      | [Licences](../../protection/licences.md)      |

## Quand en écrire un

* Choix d'une techno, d'un modèle, d'un protocole ou d'un format.
* Découpage ou fusion de composants.
* Changement incompatible d'un [contrat d'interface](../interfaces.md).

## Comment

1. Copier le [modèle](modele.md) sous `NNNN-titre-court.md`, avec le numéro suivant.
2. L'ajouter dans `SUMMARY.md` et dans l'index ci-dessus.
3. Ouvrir une PR : la discussion de la PR sert de revue de la décision.

Un ADR accepté ne se réécrit pas. Si la décision change, on écrit un nouvel ADR et on passe l'ancien en « Remplacé par ADR-NNNN ».
