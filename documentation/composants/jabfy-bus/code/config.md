# `jabfy_bus/config.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/config.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/config.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Chargement de la config du bus (JSON, YAML si disponible).

Dépôt : [jabfy-bus](README.md) · 77 lignes · statut : **actif**

Docstring du module : *Chargement de configuration (JSON natif, YAML si PyYAML est présent).*

## À retenir

- `BusConfig` l.25, `load_config` l.61.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 13 | `DEFAULT_ALLOWED_ORIGINS` | constante |
| 17 | classe `AdapterConfig` |  |
| 25 | classe `BusConfig` | Configuration racine du bus JABFY. — méthodes : `from_dict` 37 |
| 61 | `load_config()` | Charge un fichier de config .json, .yaml ou .yml. |

## Relations

- **Utilise** : [jabfy_bus/verification/policies.py](verification-policies.md)
- **Utilisé par** : [jabfy_bus/cli.py](cli.md), app/main.py (jabfy-core)
- **Testé par** : `tests/test_guard.py`, `tests/test_headless.py` → [tests de jabfy-bus](tests.md)
