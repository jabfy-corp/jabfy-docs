# `jabfy_bus/audit/log.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/audit-log.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/audit-log.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Journal d'audit chaîné par hachage : chaque message du bus y est ajouté.

Dépôt : [jabfy-bus](README.md) · 156 lignes · statut : **actif**

Docstring du module : *Journal d'audit append-only avec chaînage de hash.*

## À retenir

- `AuditLog` l.51, `attach` l.103, `verify` l.120.
- `attach` trace les messages `command.*` et `audit` : dans Core, une commande exécutée = `command.requested`, `command.approved`, `command.executed` + 1 enregistrement `command.execution` ajouté par l'ExecutionLayer (`executor.py` l.104) = 4.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 22 | `GENESIS` | constante |
| 25 | `_canonical()` |  |
| 29 | `_record_hash()` |  |
| 34 | classe `AuditRecord` | méthodes : `to_dict` 41 |
| 51 | classe `AuditLog` | Journal append-only. `path=None` = journal en mémoire (tests, simulation). — méthodes : `__init__` 54, `append` 67, `_append` 71, `record_message` 99, `attach` 103, `__len__` 110, `records` 113, `iter_bodies` 116, `verify` 120, `_load` 138 |
| 151 | `verify_file()` | Vérifie un fichier d'audit sans le charger dans un AuditLog actif. |

## Relations

- **Utilise** : [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md)
- **Utilisé par** : [jabfy_bus/api/app.py](api-app.md), [jabfy_bus/cli.py](cli.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), [jabfy_bus/verification/engine.py](verification-engine.md), app/core/bus_runtime.py (jabfy-core), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_admission.py`, `tests/test_api.py`, `tests/test_audit.py`, `tests/test_execution.py` → [tests de jabfy-bus](tests.md)
