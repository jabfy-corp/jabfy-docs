# `jabfy_bus/core/errors.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/core-errors.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/core-errors.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Exceptions du bus.

Dépôt : [jabfy-bus](README.md) · 55 lignes · statut : **actif**

Docstring du module : *Exceptions dédiées du bus JABFY.*

## À retenir

- `VerificationBypass` l.48 : levée si une commande arrive à l'exécution sans approbation.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 6 | classe `BusError` | Erreur générique du bus. |
| 10 | classe `InvalidMessage` | Le message ne respecte pas le schéma bus v1.0. — méthodes : `__init__` 13 |
| 19 | classe `AdapterError` | Erreur côté adapter protocolaire. — méthodes : `__init__` 22 |
| 28 | classe `AdapterNotReady` | L'adapter n'est pas encore utilisable (dépendance manquante, non connecté). |
| 32 | classe `UnknownProtocol` | Aucun transport/traducteur enregistré pour ce protocole. — méthodes : `__init__` 35 |
| 40 | classe `WriteNotAllowed` | Tentative d'écriture via un adapter en lecture seule. — méthodes : `__init__` 43 |
| 48 | classe `VerificationBypass` | Tentative d'exécution d'une commande non passée par le Verification Engine. — méthodes : `__init__` 51 |

## Relations

- **Utilise** : aucun fichier JABFY documenté (bibliothèques externes seulement)
- **Utilisé par** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/adapters/coap/adapter.py](coap-adapter.md), [jabfy_bus/adapters/modbus/adapter.py](modbus-adapter.md), [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md), [jabfy_bus/cli.py](cli.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/execution/translators.py](execution-translators.md)
- **Testé par** : `tests/test_admission.py`, `tests/test_execution.py`, `tests/test_message.py`, `tests/test_modbus.py`, `tests/test_mqtt_adapter.py` → [tests de jabfy-bus](tests.md)
