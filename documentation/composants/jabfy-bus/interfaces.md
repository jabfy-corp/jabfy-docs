# Interfaces

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/interfaces.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/interfaces.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

Le bus est le contrat entre les composants de Jabfy : tout ce qui entre ou sort passe par un message v1.0, décrit dans le [schéma de message](message-schema.md) et dans [`schemas/bus-message-1.0.json`](https://github.com/jabfy-corp/jabfy-bus/blob/main/schemas/bus-message-1.0.json).

## Messages produits et consommés

| Message | Produit par | Consommé par |
|---|---|---|
| `telemetry`, `state.changed`, `event` | Adapters | Registre d'entités, raisonnement, flux WebSocket |
| `health`, `capability.report` | Adapters | Abonnés (supervision, découverte) |
| `user_situation` | jabfy-core | Transporté pour le raisonnement ; aucun module du bus ne le traite |
| `command.requested` | Raisonnement (jabfy-core) | Verification Engine |
| `command.approved`, `command.rejected` | Verification Engine uniquement | Execution Layer, audit |
| `command.executed` | Execution Layer uniquement | Audit, abonnés |
| `audit` | Couche audit | Journal d'audit |
| `simulation` | Simulation Lab | Scénarios de démo |

Le bus ignore un message dont le `message_id` a déjà été vu, et l'erreur d'un abonné n'empêche jamais les autres de recevoir le message.

## Envoyer une commande

Une commande est un `command.requested` dont le champ `command` décrit l'action.

| Champ de `command` | Obligatoire | Rôle |
|---|---|---|
| `action` | Oui | Action normalisée : `turn_on`, `set_brightness`, `set_position`, `unlock`… (liste dans `core/types.py`) |
| `target` | Pour exécuter | Cible native : topic MQTT de base, URL HTTP, adresse Modbus ou appareil simulé |
| `protocol` | Pour exécuter | `mqtt`, `zigbee`, `http`, `modbus_tcp` ou `simulation` |
| `params` | Selon l'action | `brightness`, `color`, `temperature`, `position`, `tilt`, `mode` ou `value` |
| `mqtt_topic`, `http_url`, `modbus_address` | Non | Remplacent `target` pour le protocole concerné |
| `register_type` | Non | Type de registre Modbus, `coil` par défaut |

Renseigner aussi `entity` avec son `domain` : le risque d'une action dépend du domaine visé (une action sur une serrure est au moins `high`). Voir [Sécurité](security.md).

Traduction vers le protocole, pour `turn_on` :

| Protocole | Requête native |
|---|---|
| `mqtt`, `zigbee` | Publication sur `<target>/set` de `{"state": "ON"}` |
| `http` | `POST <target>?turn=on` |
| `modbus_tcp` | Écriture de `true` sur le registre `<target>` |
| `simulation` | Commande transmise telle quelle à l'appareil simulé |

Pour MQTT, les autres actions donnent `brightness`, `color`, `occupied_heating_setpoint`, `position`, `tilt` ou `system_mode`. Modbus n'accepte que `turn_on`, `turn_off` et `set_value`.

## Embarquer le bus (API Python)

C'est ce que fait jabfy-simulation dans la V0.0.1. Cet exemple tourne tel quel :

```python
from jabfy_bus.audit.log import AuditLog
from jabfy_bus.core.bus import UniversalJsonBus
from jabfy_bus.core.message import Entity, new_message
from jabfy_bus.core.types import MessageType, RiskLevel, TrustLevel
from jabfy_bus.execution.executor import ExecutionLayer
from jabfy_bus.verification.engine import VerificationEngine
from jabfy_bus.verification.policies import PolicyDecision

bus = UniversalJsonBus()
audit = AuditLog("audit.jsonl")


def authorizer(message):
    # Dans la V0.0.1, c'est ici que jabfy-simulation appelle jabfy-guard.
    return PolicyDecision("approved", "guard", "allowed by guard", RiskLevel.MEDIUM)


engine = VerificationEngine(bus, authorizer=authorizer, audit=audit)
engine.attach()

executor = ExecutionLayer(bus, audit=audit, approval_validator=engine.consume_approval)
executor.register_transport("mqtt", lambda topic, payload: print("MQTT", topic, payload))
executor.attach()

bus.publish(new_message(
    MessageType.COMMAND_REQUESTED,
    adapter="jabfy_core",
    protocol="internal",
    entity=Entity(id="light.salon", domain="light"),
    command={
        "action": "turn_on",
        "target": "zigbee2mqtt/salon_lamp",
        "protocol": "mqtt",
        "params": {},
    },
    trust_level=TrustLevel.INTERNAL,
))
# Affiche : MQTT zigbee2mqtt/salon_lamp/set {'state': 'ON'}
```

| Élément | Rôle |
|---|---|
| `UniversalJsonBus(history_size=500)` | `publish(message)`, `subscribe(pattern, handler)`, `history(pattern, limit)`. Motifs : `*`, `command.*`, type exact. |
| `VerificationEngine(bus, policies=..., authorizer=..., audit=...)` | Décide pour chaque `command.requested`. Avec un `authorizer`, sa décision remplace les policies ; s'il lève une exception, la commande est refusée. |
| `ExecutionLayer(bus, audit=..., approval_validator=...)` | Exécute les `command.approved`. Avec `approval_validator=engine.consume_approval`, chaque approbation ne sert qu'une fois, pour le message exact. |
| `register_transport(protocol, fn)` | `fn(target, payload)` envoie la requête native : c'est le seul point de contact avec le réseau. |
| `AuditLog(path=None)` | Journal chaîné ; `None` = en mémoire. Refuse de s'ouvrir sur une chaîne corrompue. |
| `EntityRegistry` | Dernier état connu de chaque entité (`attach(bus)`, `get`, `list`). |

## API HTTP et WebSocket (consultation)

Lancée par `jabfy-bus serve` (extra `api`). Elle est **en lecture seule** : aucun endpoint ne permet d'exécuter une commande.

| Méthode et chemin | Réponse |
|---|---|
| `GET /health` | `{"status": "ok", "entities": <nombre>}` |
| `GET /entities?domain=` | Entités connues, filtrables par domaine |
| `GET /entities/{entity_id}` | Une entité et son dernier message (404 si inconnue) |
| `GET /bus/history?pattern=*&limit=50` | Derniers messages du bus |
| `GET /audit?limit=50` | Derniers enregistrements d'audit |
| `GET /audit/verify` | `{"verified": true, "records": <nombre>}` |
| `WS /bus/events` | Flux de tous les messages |
| `WS /verification/decisions` | Flux des `command.*` |
| `WS /audit/live` | Flux des messages `audit` |

Une origine navigateur absente de `api.allowed_origins` est refusée : pas d'en-tête CORS en HTTP, fermeture 1008 en WebSocket. Un client sans en-tête `Origin` (CLI, service local) est accepté. Pour un service qui embarque le bus, `register_ws_routes(app, bus, allowed_origins=...)` applique la même règle.

## Ligne de commande

Voir [Installation et lancement](installation.md).
