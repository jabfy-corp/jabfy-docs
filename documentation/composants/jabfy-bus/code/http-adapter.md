# `jabfy_bus/adapters/http/adapter.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/http-adapter.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/http-adapter.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Adapter HTTP par polling : lit des endpoints REST et publie leurs valeurs.

Dépôt : [jabfy-bus](README.md) · 118 lignes · statut : **actif**

Docstring du module : *Adapter HTTP en mode polling.*

## À retenir

- `HTTPPollingAdapter` l.61, `poll_once` l.84.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 25 | `default_fetcher()` | Fetcher stdlib minimal (usage local uniquement). |
| 33 | classe `Endpoint` | Un endpoint HTTP à interroger périodiquement. |
| 46 | `dig()` | Extrait `payload["a"]["b"]` depuis un chemin "a.b". |
| 61 | classe `HTTPPollingAdapter` | Interroge des endpoints HTTP locaux et normalise les réponses. — méthodes : `__init__` 66, `start` 80, `poll_once` 84 |

## Relations

- **Utilise** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_bus_http_modbus.py` → [tests de jabfy-bus](tests.md)
