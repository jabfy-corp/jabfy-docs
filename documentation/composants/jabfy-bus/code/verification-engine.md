# `jabfy_bus/verification/engine.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/verification-engine.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/verification-engine.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — VerificationEngine : décide `approved`/`rejected` pour chaque `command.requested`.

Dépôt : [jabfy-bus](README.md) · 153 lignes · statut : **actif**

Docstring du module : *Verification Engine.*

## À retenir

- `_review` l.62 : appelle l'`authorizer` (CoreGuard ou HomeGuard) l.63-71.
- Si un authorizer est fourni, sa décision est finale : les policies internes ne sont pas consultées. Dans Core l'authorizer est `CoreGuard`.
- Sans authorizer : policies internes, aucune ne correspond → `default_deny` l.89-108.
- `_publish_decision` l.110 publie la décision sur le bus ; `consume_approval` l.149 jeton à usage unique.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 31 | classe `VerificationEngine` | Évalue chaque command.requested contre les policies. — méthodes : `__init__` 34, `attach` 51, `review` 58, `_review` 62, `_publish_decision` 110, `consume_approval` 149 |

## Relations

- **Utilise** : [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md), [jabfy_bus/verification/policies.py](verification-policies.md), [jabfy_bus/verification/risk.py](verification-risk.md)
- **Utilisé par** : [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), app/core/bus_runtime.py (jabfy-core), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_admission.py`, `tests/test_execution.py`, `tests/test_verification.py` → [tests de jabfy-bus](tests.md)
