# `jabfy_bus/adapters/mqtt/mapping.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/mqtt-mapping.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/mqtt-mapping.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Règles de correspondance topic MQTT → entité/valeur.

Dépôt : [jabfy-bus](README.md) · 98 lignes · statut : **actif**

Docstring du module : *Mapping des topics MQTT vers des entités normalisées.*

## À retenir

- `topic_matches` l.17, `TopicMapper` l.70, `extract_value` l.92.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 17 | `topic_matches()` | Match MQTT-like : `+` capture un segment, `#` capture la fin. |
| 43 | classe `TopicRule` | Règle de résolution d'un topic vers une entité. — méthodes : `resolve_entity_id` 54 |
| 64 | classe `ResolvedTopic` |  |
| 70 | classe `TopicMapper` | Résout un topic vers la première règle qui matche. — méthodes : `__init__` 73, `add` 76, `resolve` 80 |
| 92 | `extract_value()` | Extrait la valeur utile du payload sans jeter le reste. |

## Relations

- **Utilise** : [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md)
- **Testé par** : `tests/test_mqtt_adapter.py` → [tests de jabfy-bus](tests.md)
