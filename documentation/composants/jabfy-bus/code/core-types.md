# `jabfy_bus/core/types.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/core-types.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/core-types.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Énumérations du bus : types de message, niveaux de risque, niveaux de confiance.

Dépôt : [jabfy-bus](README.md) · 158 lignes · statut : **actif**

Docstring du module : *Types et énumérations partagés par tout le bus.*

## À retenir

- `TrustLevel` l.112 : 5 valeurs ; Core utilise `INTERNAL` pour l'utilisateur **et** le headless.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 13 | classe `MessageType` | Types de messages circulant sur le bus. |
| 30 | classe `Domain` | Domaines d'entités normalisés. |
| 54 | classe `EntityClass` | Classes sémantiques : le sens réel de la donnée. |
| 86 | classe `Action` | Actions normalisées, indépendantes du protocole cible. |
| 112 | classe `TrustLevel` | Niveau de confiance de la source d'un message. — méthodes : `rank` 121 |
| 125 | `_TRUST_RANK` | constante |
| 134 | classe `RiskLevel` | Niveaux de risque d'une commande. — méthodes : `rank` 142 |
| 146 | `_RISK_RANK` | constante |
| 154 | classe `AdapterMode` | Mode d'un adapter. Par défaut : lecture seule. |

## Relations

- **Utilise** : aucun fichier JABFY documenté (bibliothèques externes seulement)
- **Utilisé par** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/adapters/coap/adapter.py](coap-adapter.md), [jabfy_bus/adapters/http/adapter.py](http-adapter.md), [jabfy_bus/adapters/http/webhook.py](http-webhook.md), [jabfy_bus/adapters/modbus/adapter.py](modbus-adapter.md), [jabfy_bus/adapters/modbus/registers.py](modbus-registers.md), [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md), [jabfy_bus/adapters/mqtt/mapping.py](mqtt-mapping.md), [jabfy_bus/adapters/zigbee2mqtt/adapter.py](zigbee2mqtt-adapter.md), [jabfy_bus/adapters/zigbee2mqtt/devices.py](zigbee2mqtt-devices.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/execution/translators.py](execution-translators.md), [jabfy_bus/simulation/devices.py](simulation-devices.md), [jabfy_bus/simulation/lab.py](simulation-lab.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), [jabfy_bus/verification/engine.py](verification-engine.md), [jabfy_bus/verification/policies.py](verification-policies.md), [jabfy_bus/verification/risk.py](verification-risk.md), app/api/routes_bus.py (jabfy-core), app/core/action_orchestrator.py (jabfy-core), app/core/guard.py (jabfy-core), sim/dashboard/commands.py (jabfy-simulation), sim/dashboard/guard.py (jabfy-simulation), sim/integration/bus_runner.py (jabfy-simulation), sim/integration/reflex.py (jabfy-simulation)
- **Testé par** : `tests/test_admission.py`, `tests/test_api.py`, `tests/test_bus.py`, `tests/test_bus_http_modbus.py`, `tests/test_execution.py`, `tests/test_guard.py`, `tests/test_headless.py`, `tests/test_message.py`, `tests/test_modbus.py`, `tests/test_mqtt_adapter.py`, `tests/test_reflex.py`, `tests/test_verification.py` → [tests de jabfy-bus](tests.md)
