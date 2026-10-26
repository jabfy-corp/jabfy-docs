# Interfaces

Les repos ne se parlent qu'à travers des contrats versionnés. Toute modification d'un contrat passe par une PR sur le repo qui le possède, et par un ADR si elle casse la compatibilité.

| Contrat | Propriétaire | Format | Source de vérité |
|---|---|---|---|
| Messages du bus | jabfy-bus | JSON Schema 2020-12 | [`schemas/bus-message-1.0.json`](https://github.com/jabfy-corp/jabfy-bus/blob/main/schemas/bus-message-1.0.json) |
| API HTTP de Core | jabfy-core | OpenAPI, générée par FastAPI | `/openapi.json` de l'API en marche |
| Autorisation des commandes | jabfy-guard | API Python (`evaluate`, `load_policies`) | [README de jabfy-guard](https://github.com/jabfy-corp/jabfy-guard) |
| Synthèse vocale | jabfy-tts | API TypeScript (`JabfyTTS`) | [README de jabfy-tts](https://github.com/jabfy-corp/jabfy-tts) |

## Le bus, contrat entre tous les repos

Champs obligatoires : `bus_version`, `message_id`, `timestamp`, `message_type`, `source`.

| `message_type` | Sens |
|---|---|
| `telemetry` | Mesure remontée par un appareil |
| `state.changed` | Changement d'état d'une entité |
| `event` | Événement ponctuel |
| `command.requested` | Action proposée, en attente de vérification |
| `command.approved` / `command.rejected` | Décision de la vérification |
| `command.executed` | Action effectuée sur l'appareil |
| `capability.report` | Capacités déclarées par un appareil |
| `health` | État de santé d'un composant |
| `audit` | Entrée du journal d'audit |
| `simulation` | Message propre au simulateur |
| `user_situation` | Consigne de l'utilisateur envoyée par Core, entrée du raisonnement (PR jabfy-bus#6) |

Le schéma détaillé est documenté dans `docs/message-schema.md` de jabfy-bus (visible dans [Composants](../composants/README.md) une fois jabfy-bus agrégé).

### Règles de version proposées

- `bus_version` vaut aujourd'hui `"1.0"`.
- Ajouter un champ **optionnel** ou une nouvelle valeur de `message_type` : version mineure, compatible.
- Supprimer, renommer ou rendre obligatoire un champ : version majeure, nouveau fichier `bus-message-2.0.json`, ADR obligatoire.
- Les deux versions coexistent tant qu'un repo consomme encore l'ancienne.

## À mettre en place

- [ ] Générer la doc de référence du bus à partir de `schemas/` dans `docs/reference/` de jabfy-bus, en CI, pour qu'elle soit agrégée automatiquement.
- [ ] Exporter l'OpenAPI de Core dans `docs/openapi.json` en CI, et l'afficher dans GitBook avec un bloc OpenAPI.
- [ ] Valider en CI les exemples de messages contre le schéma (`jabfy-bus validate`).
