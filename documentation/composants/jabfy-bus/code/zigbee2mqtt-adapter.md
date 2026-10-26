# `jabfy_bus/adapters/zigbee2mqtt/adapter.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/zigbee2mqtt-adapter.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/zigbee2mqtt-adapter.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Adapter Zigbee2MQTT : transforme les messages `zigbee2mqtt/<device>` en messages bus.

Dépôt : [jabfy-bus](README.md) · 158 lignes · statut : **actif**

Docstring du module : *Adapter Zigbee2MQTT.*

## À retenir

- `handle_mqtt` l.67 ; ignore les topics `/set` l.74-76 (ce sont nos propres commandes).

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 28 | classe `Zigbee2MQTTAdapter` | Traduit les topics `zigbee2mqtt/<friendly_name>` vers le bus. — méthodes : `__init__` 33, `start` 46, `register_device` 52, `handle_mqtt` 67, `_emit_exposes` 87, `_handle_availability` 131, `_handle_bridge` 139 |

## Relations

- **Utilise** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md), [jabfy_bus/adapters/zigbee2mqtt/devices.py](zigbee2mqtt-devices.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : app/core/bus_runtime.py (jabfy-core), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_zigbee2mqtt.py` → [tests de jabfy-bus](tests.md)
