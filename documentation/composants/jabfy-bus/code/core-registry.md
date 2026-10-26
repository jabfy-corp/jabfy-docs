# `jabfy_bus/core/registry.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/core-registry.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/core-registry.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — `EntityRegistry` : dernier état connu de chaque entité vue sur le bus.

Dépôt : [jabfy-bus](README.md) · 73 lignes · statut : **actif**

Docstring du module : *Registre d'entités : dernier état connu de chaque entité du bus.*

## À retenir

- `observe` l.46 écoute telemetry/state/capability.
- N'est pas consulté par guard pour recouper l'inventaire du simulateur.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 13 | classe `EntityRecord` | méthodes : `last_value` 24, `last_seen` 30 |
| 34 | classe `EntityRegistry` | Suit les entités observées via telemetry / state / capability. — méthodes : `__init__` 39, `attach` 42, `observe` 46, `get` 63, `list` 66, `__len__` 72 |

## Relations

- **Utilise** : [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md)
- **Utilisé par** : [jabfy_bus/api/app.py](api-app.md), [jabfy_bus/cli.py](cli.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), app/core/bus_runtime.py (jabfy-core), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_api.py` → [tests de jabfy-bus](tests.md)
