# `sim/dashboard/defaults.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-simulation/docs/code/dashboard-defaults.md](https://github.com/jabfy-corp/jabfy-simulation/blob/main/docs/code/dashboard-defaults.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Maison par défaut du dashboard (7 appareils, règle mouvement → lumière).

Dépôt : [jabfy-simulation](README.md) · 35 lignes · statut : **actif**

Docstring du module : *Small built-in home, usable from an installed wheel without a config file.*

## À retenir

- `home_config`.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 6 | `home_config()` |  |

## Relations

- **Utilise** : [sim/config/schema.py](config-schema.md)
- **Utilisé par** : aucun import direct (point d'entrée, appelé par HTTP, CLI ou navigateur)
- **Testé par** : `tests/test_home.py` → [tests de jabfy-simulation](tests.md)
