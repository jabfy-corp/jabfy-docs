# `jabfy_bus/simulation/lab.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/simulation-lab.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/simulation-lab.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Labo de simulation du bus : relie appareils simulés et transport.

Dépôt : [jabfy-bus](README.md) · 115 lignes · statut : **actif**

Docstring du module : *Simulation Lab.*

## À retenir

- `SimulationLab` l.65, transport l.102.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 22 | classe `SimulationAdapter` | Adapter du lab : publie les lectures simulées sur le bus. — méthodes : `__init__` 27, `start` 35, `emit_reading` 39 |
| 65 | classe `SimulationLab` | Orchestre les devices simulés et le temps discret du lab. — méthodes : `__init__` 68, `add_device` 75, `get` 79, `tick` 84, `run` 94, `transport` 102 |

## Relations

- **Utilise** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md), [jabfy_bus/simulation/devices.py](simulation-devices.md)
- **Utilisé par** : [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md)
- **Testé par** : `tests/test_simulation.py` → [tests de jabfy-bus](tests.md)
