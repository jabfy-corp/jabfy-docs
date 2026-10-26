# `jabfy_bus/execution/translators.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/execution-translators.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/execution-translators.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Traduit une commande JSON en message protocole (ex. payload MQTT `/set`).

Dépôt : [jabfy-bus](README.md) · 108 lignes · statut : **actif**

Docstring du module : *Traducteurs : commande normalisée -> requête native par protocole.*

## À retenir

- `to_mqtt` l.30 : topic + `/set`, `turn_on` → `{"state": "ON"}`, `set_temperature` → `occupied_heating_setpoint`.
- Table `TRANSLATORS` l.95.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 23 | `_MQTT_STATE` | constante |
| 30 | `to_mqtt()` |  |
| 54 | `_HTTP_TURN` | constante |
| 57 | `to_http()` |  |
| 73 | `to_modbus()` |  |
| 90 | `to_simulation()` | Le lab de simulation consomme la commande normalisée telle quelle. |
| 104 | `translate()` |  |

## Relations

- **Utilise** : [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/execution/executor.py](execution-executor.md), sim/integration/bus_runner.py (jabfy-simulation)
- **Testé par** : `tests/test_execution.py` → [tests de jabfy-bus](tests.md)
