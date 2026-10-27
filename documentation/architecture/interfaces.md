# Interfaces

Les repos ne se parlent qu'à travers des contrats. Toute modification d'un contrat passe par une PR sur le repo qui le possède, et par un ADR si elle casse la compatibilité.

## Carte des contrats

| Contrat | Propriétaire | Format | Consommateurs | Source de vérité |
|---|---|---|---|---|
| Messages du bus | jabfy-bus | JSON Schema 2020-12, `bus_version` 1.0 | Adapters, Core, simulation | [`schemas/bus-message-1.0.json`](https://github.com/jabfy-corp/jabfy-bus/blob/main/schemas/bus-message-1.0.json) |
| API de proposition | jabfy-core | HTTP/JSON, OpenAPI générée par FastAPI | Clients, simulation | `/openapi.json` de Core |
| Inventaire de la maison | jabfy-simulation | HTTP/JSON (`GET /api/ai/context`) | Core | [Interfaces de jabfy-simulation](../composants/README.md) |
| Topics des appareils | Zigbee2MQTT, émulé par la simulation | MQTT : `zigbee2mqtt/<id>` (état), `zigbee2mqtt/<id>/set` (commande) | jabfy-bus | Convention Zigbee2MQTT |
| Autorisation des commandes | jabfy-guard | API Python (`evaluate`, `load_policies`) | jabfy-bus (`authorizer`) | Branche `guard-4-v001-deployment` |
| Synthèse vocale | jabfy-tts | API Rust (`JabfyTts`, `TtsStream`) | Core (prévu) | [Interfaces de jabfy-tts](../composants/README.md) |
| Suivi de la voix | jabfy-voice | HTTP/JSON (`GET /state`) | Interface web de la voix | [Interfaces de jabfy-voice](../composants/README.md) |
| Serveur de modèles | Ollama / llama.cpp | API compatible OpenAI | Core, voice | Spécification OpenAI Chat Completions |

## Le bus, contrat entre tous les composants

Champs obligatoires : `bus_version`, `message_id`, `timestamp`, `message_type`, `source`. Toute donnée brute est conservée à côté de la valeur normalisée.

| `message_type` | Sens | Produit par |
|---|---|---|
| `telemetry`, `state.changed`, `event` | Mesure, changement d'état, événement d'un appareil | Adapters |
| `capability.report`, `health` | Capacités déclarées, santé d'un composant | Adapters |
| `user_situation` | Consigne de l'utilisateur, entrée du raisonnement | Core |
| `command.requested` | Action proposée, en attente de vérification | Raisonnement (Core) |
| `command.approved`, `command.rejected` | Décision de la vérification | Verification Engine uniquement |
| `command.executed` | Action effectuée sur l'appareil | Execution Layer uniquement |
| `audit` | Entrée du journal d'audit | Couche audit |
| `simulation` | Message propre au simulateur | Simulation Lab |

### Règles de version

- Ajouter un champ **optionnel** ou une valeur de `message_type` : version mineure, compatible.
- Supprimer, renommer ou rendre obligatoire un champ : version majeure, nouveau fichier `bus-message-2.0.json`, ADR obligatoire.
- Les deux versions coexistent tant qu'un composant consomme encore l'ancienne.

## L'API de Core : trois versions à réconcilier

Le contrat entre Core et ses appelants n'est pas encore stabilisé. Selon la branche :

| Branche de jabfy-core | Route | Utilisée par |
|---|---|---|
| `main` | `POST /act` : situation + état des appareils → proposition vérifiée | Clients (prévu) |
| `core-3-publish-container-image` (V0.0.1) | `POST /simulation/propose` | Panneau IA de jabfy-simulation (`/api/ai/propose`) |
| `core-12-bus-integration` | `POST /prompt`, `GET /prompts/{id}` : exécution suivie, bus embarqué | Panneau IA de jabfy-simulation (`/api/ai/prompt`) |

**Décision à prendre** : choisir le contrat cible, le documenter en OpenAPI, puis aligner la simulation et les clients dessus.

## À mettre en place

- [ ] Choisir et figer l'API de Core (voir ci-dessus), puis publier son OpenAPI dans la doc.
- [ ] Générer la doc de référence des messages du bus à partir de `schemas/`, en CI.
- [ ] Valider en CI les exemples de messages contre le schéma (`jabfy-bus validate`).
- [ ] Fusionner la bibliothèque jabfy-guard sur `main` et documenter son API.
