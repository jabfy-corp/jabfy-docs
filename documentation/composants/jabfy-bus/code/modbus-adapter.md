# `jabfy_bus/adapters/modbus/adapter.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/modbus-adapter.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/modbus-adapter.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Adapter Modbus : lit des registres et écrit des consignes.

Dépôt : [jabfy-bus](README.md) · 136 lignes · statut : **actif**

Docstring du module : *Adapter Modbus TCP.*

## À retenir

- `ModbusAdapter` l.30, `poll_once` l.64, `write_register` l.128.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 26 | classe `ModbusWriter` | méthodes : `write` 27 |
| 30 | classe `ModbusAdapter` | Poll les registres d'un RegisterMap et publie les valeurs décodées. — méthodes : `__init__` 35, `start` 55, `poll_once` 64, `_emit_register` 86, `write_register` 128 |

## Relations

- **Utilise** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/adapters/modbus/registers.py](modbus-registers.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_bus_http_modbus.py`, `tests/test_modbus.py` → [tests de jabfy-bus](tests.md)
