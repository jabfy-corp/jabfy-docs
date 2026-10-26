# `jabfy_bus/api/ws.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/api-ws.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/api-ws.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — WebSocket `/bus/events` : diffuse en direct les messages du bus.

Dépôt : [jabfy-bus](README.md) · 97 lignes · statut : **actif**

Docstring du module : *Flux WebSocket temps réel des événements du bus.*

## À retenir

- `register_ws_routes` l.55, vérifie l'origine.
- Réutilisé par Core (`main.py` l.83).

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 16 | classe `BusEventStream` | Pont bus synchrone -> file asyncio consommable par un WebSocket. — méthodes : `__init__` 19, `start` 31, `stop` 34, `_enqueue` 39, `next_event` 51 |
| 55 | `register_ws_routes()` | Ajoute les endpoints WebSocket à une app FastAPI existante. |

## Relations

- **Utilise** : [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md)
- **Utilisé par** : [jabfy_bus/cli.py](cli.md), app/main.py (jabfy-core)
- **Testé par** : `tests/test_api.py` → [tests de jabfy-bus](tests.md)
