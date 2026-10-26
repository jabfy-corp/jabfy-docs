# `jabfy_bus/execution/executor.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/execution-executor.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/execution-executor.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — ExecutionLayer : exécute une commande approuvée via le transport du protocole.

Dépôt : [jabfy-bus](README.md) · 120 lignes · statut : **actif**

Docstring du module : *Execution Layer.*

## À retenir

- `execute` l.49 ; `VerificationBypass` l.51-56 si le message n'est pas un `command.approved` émis par `verification_engine`, ou si l'`approval_validator` refuse.
- Core ne passe pas d'`approval_validator` (pas de jeton à usage unique) ; le simulateur passe `consume_approval`.
- `translate` → transport du protocole ; une exception devient un résultat `failed`, pas un crash l.72-76.
- `_publish_result` l.80 publie `command.executed`/`failed`.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 27 | classe `ExecutionLayer` | Exécute les commandes approuvées via les transports enregistrés. — méthodes : `__init__` 30, `register_transport` 39, `attach` 42, `execute` 49, `_publish_result` 80 |

## Relations

- **Utilise** : [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md), [jabfy_bus/execution/translators.py](execution-translators.md)
- **Utilisé par** : [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), app/core/bus_runtime.py (jabfy-core), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_admission.py`, `tests/test_execution.py` → [tests de jabfy-bus](tests.md)
