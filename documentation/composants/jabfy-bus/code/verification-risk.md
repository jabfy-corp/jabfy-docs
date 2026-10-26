# `jabfy_bus/verification/risk.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/verification-risk.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/verification-risk.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Table de risque du bus : risque de base par action et plancher par domaine.

Dépôt : [jabfy-bus](README.md) · 73 lignes · statut : **actif**

Docstring du module : *Classification du risque des commandes.*

## À retenir

- `ACTION_BASE_RISK` l.17-39, `DOMAIN_MIN_RISK` l.42-49, `classify_risk` l.56.
- Ne pas confondre avec la table de jabfy-guard (`risk.py` du guard).

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 52 | `_max_risk()` |  |
| 56 | `classify_risk()` | Risque d'une commande = max(risque action, plancher du domaine cible). |

## Relations

- **Utilise** : [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/verification/engine.py](verification-engine.md), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_verification.py` → [tests de jabfy-bus](tests.md)
