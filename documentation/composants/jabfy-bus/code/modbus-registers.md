# `jabfy_bus/adapters/modbus/registers.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/modbus-registers.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/modbus-registers.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Description des registres Modbus (type, échelle, encodage).

Dépôt : [jabfy-bus](README.md) · 85 lignes · statut : **actif**

Docstring du module : *Register map Modbus avec sémantique.*

## À retenir

- `RegisterSpec` l.28 decode/encode, `RegisterMap` l.58.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 16 | classe `RegisterType` | méthodes : `writable_type` 23 |
| 28 | classe `RegisterSpec` | Sémantique d'un registre Modbus. — méthodes : `decode` 42, `encode` 51 |
| 58 | classe `RegisterMap` | Ensemble des registres connus d'un équipement (unit_id). — méthodes : `__init__` 61, `add` 67, `get` 75, `specs` 78, `readable` 81, `writable` 84 |

## Relations

- **Utilise** : [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/adapters/modbus/adapter.py](modbus-adapter.md), sim/integration/bus_runner.py (jabfy-simulation), sim/integration/modbus_client.py (jabfy-simulation)
- **Testé par** : `tests/test_bus_http_modbus.py`, `tests/test_modbus.py` → [tests de jabfy-bus](tests.md)
