# `jabfy_bus/adapters/coap/adapter.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/coap-adapter.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/coap-adapter.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Squelette d'adapter CoAP, prévu pour plus tard.

Dépôt : [jabfy-bus](README.md) · 62 lignes · statut : **squelette (phase 2)**

Docstring du module : *Squelette d'adapter CoAP (P2).*

## À retenir

- `CoAPAdapter` l.28.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 19 | `coap_uri_to_entity()` | `coap://sensor-01/temp` -> (device_id, resource). |
| 28 | classe `CoAPAdapter` | Contrat de l'adapter CoAP. Transport non implémenté (P2). — méthodes : `__init__` 33, `start` 41, `handle_response` 44 |

## Relations

- **Utilise** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : aucun import direct (point d'entrée, appelé par HTTP, CLI ou navigateur)
