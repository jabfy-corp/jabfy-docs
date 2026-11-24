# `app/schemas/generation.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-core/docs/code/schemas-generation.md](https://github.com/jabfy-corp/jabfy-core/blob/main/docs/code/schemas-generation.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — `GenerationParams` : paramètres d'échantillonnage (température, etc.) envoyés au backend.

Dépôt : [jabfy-core](README.md) · 28 lignes · statut : **actif**

## À retenir

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 6 | classe `GenerationParams` | Sampling parameters forwarded to llama.cpp. — méthodes : `to_payload` 27 |

## Relations

- **Utilise** : aucun fichier JABFY documenté (bibliothèques externes seulement)
- **Utilisé par** : [app/core/llm_client.py](llm-client.md), [app/core/openai_client.py](openai-client.md), [app/schemas/actions.py](schemas-actions.md), [app/simulation/planner.py](simulation-planner.md)
- **Testé par** : `tests/test_generation_params.py`, `tests/test_openai_client.py` → [tests de jabfy-core](tests.md)
