# `jabfy_bus/adapters/zigbee2mqtt/devices.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/zigbee2mqtt-devices.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/zigbee2mqtt-devices.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Connaissance des modèles Zigbee2MQTT : correspondance des « exposes » vers les entités.

Dépôt : [jabfy-bus](README.md) · 101 lignes · statut : **actif**

Docstring du module : *Connaissance des devices Zigbee2MQTT.*

## À retenir

- `ExposeMapping` l.15, `DeviceInfo` l.70, `normalize_expose_value` l.92.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 15 | classe `ExposeMapping` |  |
| 56 | `IGNORED_KEYS` | constante |
| 70 | classe `DeviceInfo` | Fiche minimale d'un modèle connu. |
| 92 | `normalize_expose_value()` | Normalise la valeur d'un expose (inversion des booléens 'contact'). |

## Relations

- **Utilise** : [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/adapters/zigbee2mqtt/adapter.py](zigbee2mqtt-adapter.md)
