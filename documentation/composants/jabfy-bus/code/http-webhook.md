# `jabfy_bus/adapters/http/webhook.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/http-webhook.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/http-webhook.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Réception de webhooks HTTP entrants.

Dépôt : [jabfy-bus](README.md) · 103 lignes · statut : **actif**

Docstring du module : *Réception de webhooks HTTP entrants.*

## À retenir

- `WebhookReceiver` l.33.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 28 | classe `WebhookRoute` |  |
| 33 | classe `WebhookReceiver` | Adapter webhook : chaque route a son normaliseur dédié. — méthodes : `__init__` 38, `route` 54, `handle_payload` 60, `start` 74, `stop` 99 |

## Relations

- **Utilise** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : aucun import direct (point d'entrée, appelé par HTTP, CLI ou navigateur)
