# `jabfy_bus/verification/policies.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/verification-policies.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/verification-policies.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Policies déclaratives du bus (domaines, actions, risque max, confiance min, fenêtre horaire).

Dépôt : [jabfy-bus](README.md) · 98 lignes · statut : **actif**

Docstring du module : *Policies du Verification Engine.*

## À retenir

- `Policy` l.45 + `matches` l.58 ; `policy_from_dict` l.82 lit `config/bus.json`.
- `TimeWindow` l.20 gère les fenêtres passant minuit.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 20 | classe `TimeWindow` | Fenêtre horaire locale, gère les fenêtres passant minuit (22h -> 6h). — méthodes : `contains` 26 |
| 33 | classe `PolicyDecision` | méthodes : `approved` 40 |
| 45 | classe `Policy` | Règle déclarative de validation de commande. — méthodes : `matches` 58 |
| 82 | `policy_from_dict()` | Construit une policy depuis une config JSON/YAML. |

## Relations

- **Utilise** : [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/config.py](config.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), [jabfy_bus/verification/engine.py](verification-engine.md), app/core/bus_runtime.py (jabfy-core), app/core/guard.py (jabfy-core), sim/dashboard/guard.py (jabfy-simulation), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_admission.py`, `tests/test_execution.py`, `tests/test_verification.py` → [tests de jabfy-bus](tests.md)
