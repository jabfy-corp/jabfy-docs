# `jabfy_bus/adapters/base.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/base.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/base.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — `BaseAdapter` : socle commun des adapters protocolaires (émission, santé, écriture).

Dépôt : [jabfy-bus](README.md) · 90 lignes · statut : **actif**

Docstring du module : *Classe de base des adapters protocolaires.*

## À retenir

- `emit` l.57, `ensure_writable` l.77, `write` l.82.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 23 | classe `BaseAdapter` | Socle commun à tous les adapters. — méthodes : `__init__` 28, `start` 44, `stop` 47, `running` 52, `emit` 57, `report_health` 65, `ensure_writable` 77, `write` 82, `make_source` 89 |

## Relations

- **Utilise** : [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/adapters/coap/adapter.py](coap-adapter.md), [jabfy_bus/adapters/http/adapter.py](http-adapter.md), [jabfy_bus/adapters/http/webhook.py](http-webhook.md), [jabfy_bus/adapters/modbus/adapter.py](modbus-adapter.md), [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md), [jabfy_bus/adapters/zigbee2mqtt/adapter.py](zigbee2mqtt-adapter.md), [jabfy_bus/simulation/lab.py](simulation-lab.md)
