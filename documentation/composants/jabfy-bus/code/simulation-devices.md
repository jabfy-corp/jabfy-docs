# `jabfy_bus/simulation/devices.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/simulation-devices.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/simulation-devices.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Appareils simulés minimalistes internes au bus (pour ses tests et démos).

Dépôt : [jabfy-bus](README.md) · 174 lignes · statut : **actif**

Docstring du module : *Devices simulés pour le Simulation Lab.*

## À retenir

- `SimulatedMotionSensor` l.75, `SimulatedSwitch` l.109.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 18 | classe `Reading` | Une mesure produite par un device simulé. |
| 30 | classe `SimulatedDevice` | Device virtuel piloté par le lab. — méthodes : `__init__` 33, `tick` 39 |
| 43 | classe `SimulatedTemperatureSensor` | Marche aléatoire bornée autour d'une température de consigne. — méthodes : `__init__` 46, `tick` 59 |
| 75 | classe `SimulatedMotionSensor` | Détection de mouvement probabiliste, avec possibilité de forcer. — méthodes : `__init__` 78, `force` 89, `tick` 93 |
| 109 | classe `SimulatedSwitch` | Actionneur on/off : reçoit des commandes du lab. — méthodes : `__init__` 112, `apply_command` 117, `tick` 126 |
| 139 | classe `SimulatedPowerMeter` | Compteur : puissance instantanée bruitée + énergie cumulée. — méthodes : `__init__` 142, `tick` 153 |

## Relations

- **Utilise** : [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/simulation/lab.py](simulation-lab.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md)
- **Testé par** : `tests/test_simulation.py` → [tests de jabfy-bus](tests.md)
