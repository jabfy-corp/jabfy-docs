# `jabfy_bus/cli.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/cli.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/cli.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Commande `jabfy-bus` : `demo`, `validate`, `audit-verify`, `serve`.

Dépôt : [jabfy-bus](README.md) · 127 lignes · statut : **actif**

Docstring du module : *CLI du bus JABFY.*

## À retenir

- `cmd_serve` l.59 : hôte par défaut 127.0.0.1, port `JABFY_BUS_PORT` 8080.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 24 | `cmd_demo()` |  |
| 39 | `cmd_validate()` |  |
| 53 | `cmd_audit_verify()` |  |
| 59 | `cmd_serve()` |  |
| 92 | `build_parser()` |  |
| 120 | `main()` |  |

## Relations

- **Utilise** : [jabfy_bus/api/app.py](api-app.md), [jabfy_bus/api/ws.py](api-ws.md), [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/config.py](config.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/registry.py](core-registry.md), [jabfy_bus/logging_utils.py](logging-utils.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md)
- **Utilisé par** : aucun import direct (point d'entrée, appelé par HTTP, CLI ou navigateur)
