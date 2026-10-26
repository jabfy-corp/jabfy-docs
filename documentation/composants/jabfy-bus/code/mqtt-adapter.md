# `jabfy_bus/adapters/mqtt/adapter.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/mqtt-adapter.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/mqtt-adapter.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Adapter MQTT générique : topics → télémétrie via des règles de mapping.

Dépôt : [jabfy-bus](README.md) · 134 lignes · statut : **actif**

Docstring du module : *Adapter MQTT.*

## À retenir

- `MQTTAdapter` l.43, `handle_message` l.82 → TELEMETRY, `write` l.128 en qos 1.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 24 | classe `MQTTClient` | Interface minimale attendue d'un client MQTT. — méthodes : `connect` 27, `disconnect` 28, `subscribe` 29, `publish` 30 |
| 33 | `parse_payload()` | Décode un payload MQTT : JSON si possible, scalaire sinon. |
| 43 | classe `MQTTAdapter` | Traduit les messages MQTT entrants vers le bus JSON. — méthodes : `__init__` 48, `start` 66, `stop` 75, `handle_message` 82, `write` 128 |

## Relations

- **Utilise** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/adapters/mqtt/mapping.py](mqtt-mapping.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/adapters/zigbee2mqtt/adapter.py](zigbee2mqtt-adapter.md)
- **Testé par** : `tests/test_mqtt_adapter.py` → [tests de jabfy-bus](tests.md)
