# `app/api/routes_models.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-core/docs/code/routes-models.md](https://github.com/jabfy-corp/jabfy-core/blob/main/docs/code/routes-models.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — `GET /models` : liste les modèles exposés par le backend LLM.

Dépôt : [jabfy-core](README.md) · 23 lignes · statut : **actif**

## À retenir

- `get_models` l.13 appelle `llm_client.list_models()`, `LLMClientError` → 502.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 13 | `get_models()` |  |

## Relations

- **Utilise** : [app/core/errors.py](errors.md), [app/schemas/models.py](schemas-models.md)
- **Utilisé par** : [app/main.py](main.md)
