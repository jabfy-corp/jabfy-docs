# Schéma de message — bus v1.0

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/message-schema.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/message-schema.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

Le schéma machine est dans [`schemas/bus-message-1.0.json`](https://github.com/jabfy-corp/jabfy-bus/blob/main/schemas/bus-message-1.0.json).
L'implémentation de référence est `jabfy_bus/core/message.py`.

## Exemple complet

```json
{
  "bus_version": "1.0",
  "message_id": "3fc9…",
  "correlation_id": null,
  "timestamp": "2026-06-25T10:00:00+02:00",
  "message_type": "state.changed",
  "source": {
    "adapter": "mqtt_adapter",
    "protocol": "mqtt",
    "bridge": "zigbee2mqtt",
    "raw_address": "zigbee2mqtt/salon/temp",
    "device_id": "salon_temp_01"
  },
  "entity": {
    "id": "sensor.salon_temperature",
    "domain": "sensor",
    "class": "temperature",
    "location": "salon",
    "asset": null
  },
  "value": {
    "raw": 217,
    "normalized": 21.7,
    "unit": "°C",
    "datatype": "float",
    "scale": 0.1
  },
  "capabilities": ["read", "subscribe"],
  "quality": { "confidence": 1.0, "source_quality": "good", "stale": false },
  "security": {
    "trust_level": "local_gateway",
    "auth_context": "adapter_service_account",
    "verified": true,
    "write_allowed": false
  },
  "raw": {
    "topic": "zigbee2mqtt/salon/temp",
    "payload": { "temperature": 21.7, "battery": 87 }
  }
}
```

## Champs indispensables

| Champ | Pourquoi |
|---|---|
| `message_id` | Audit, déduplication (le bus ignore les doublons) |
| `correlation_id` | Relie requête → décision → exécution |
| `source.protocol` | Savoir d'où vient l'info |
| `source.raw_address` | Debug et traçabilité |
| `entity.domain` / `entity.class` | Normalisation logique + sens réel |
| `value.raw` / `value.normalized` | Ne jamais perdre l'origine |
| `security.trust_level` | Entrée de la décision de risque |
| `capabilities` | Lire / écrire / commander |
| `raw` | Sauvegarde forensic du payload natif |

## Types de messages

| Type | Émis par |
|---|---|
| `telemetry` | Adapters (mesures) |
| `state.changed` | Adapters (état on/off, position…) |
| `event` | Adapters (événement ponctuel) |
| `command.requested` | Reasoning (proposition, jamais une exécution) |
| `command.approved` / `command.rejected` | Verification Engine uniquement |
| `command.executed` | Execution Layer uniquement |
| `capability.report` | Adapters (découverte) |
| `health` | Adapters (état de l'adapter/device) |
| `audit` | Couche audit |
| `simulation` | Simulation Lab |
| `user_situation` | Core (consigne utilisateur, entrée du raisonnement) |

## Anti-patterns

Interdit — payload pauvre qui détruit le contexte :

```json
{ "temperature": 21.7 }
```

Interdit — exécution directe sans vérification :

```text
Reasoning -> MQTT publish
```
