# `jabfy_bus/api/app.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/api-app.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/api-app.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — API HTTP de lecture du bus (mode service autonome).

Dépôt : [jabfy-bus](README.md) · 99 lignes · statut : **actif**

Docstring du module : *API HTTP de consultation (lecture seule).*

## À retenir

- Routes GET seulement.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 19 | `_require_fastapi()` |  |
| 29 | `create_app()` | Construit l'application FastAPI branchée sur le bus. |

## Relations

- **Utilise** : [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/registry.py](core-registry.md)
- **Utilisé par** : [jabfy_bus/cli.py](cli.md)
- **Testé par** : `tests/test_api.py` → [tests de jabfy-bus](tests.md)
