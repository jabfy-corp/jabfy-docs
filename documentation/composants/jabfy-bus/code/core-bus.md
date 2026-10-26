# `jabfy_bus/core/bus.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/core-bus.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/core-bus.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Le bus lui-même : `UniversalJsonBus`, publication/abonnement de `BusMessage` en mémoire.

Dépôt : [jabfy-bus](README.md) · 107 lignes · statut : **actif**

Docstring du module : *Bus pub/sub interne (in-process).*

## À retenir

- `publish` l.72 : valide, déduplique par `message_id` l.79-82, puis dispatch **synchrone** l.86-98.
- Ordre : abonnés dans l'ordre d'abonnement ; si un abonné publie, le nouveau message est traité **avant** de revenir (profondeur d'abord).
- Conséquence : `publish(command.requested)` revient seulement quand décision, exécution et résultat sont faits.
- C'est ce qui oblige le journal des runs de jabfy-core à classer les statuts d'étape (`STEP_RANK`).

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 26 | `match_pattern()` | Match par segments séparés par des points, `*` = joker. |
| 43 | classe `Subscription` |  |
| 49 | classe `UniversalJsonBus` | Bus JSON universel : point de passage unique des messages. — méthodes : `__init__` 52, `subscribe` 59, `unsubscribe` 64, `publish` 72, `history` 103 |

## Relations

- **Utilise** : [jabfy_bus/core/message.py](core-message.md)
- **Utilisé par** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/adapters/coap/adapter.py](coap-adapter.md), [jabfy_bus/adapters/http/adapter.py](http-adapter.md), [jabfy_bus/adapters/http/webhook.py](http-webhook.md), [jabfy_bus/adapters/modbus/adapter.py](modbus-adapter.md), [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md), [jabfy_bus/adapters/zigbee2mqtt/adapter.py](zigbee2mqtt-adapter.md), [jabfy_bus/api/app.py](api-app.md), [jabfy_bus/api/ws.py](api-ws.md), [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/cli.py](cli.md), [jabfy_bus/core/registry.py](core-registry.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/simulation/lab.py](simulation-lab.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), [jabfy_bus/verification/engine.py](verification-engine.md), app/core/bus_runtime.py (jabfy-core), app/core/run_journal.py (jabfy-core), sim/integration/bus_runner.py (jabfy-simulation), sim/integration/reflex.py (jabfy-simulation)
- **Testé par** : `tests/test_admission.py`, `tests/test_api.py`, `tests/test_bus.py`, `tests/test_bus_http_modbus.py`, `tests/test_dashboard.py`, `tests/test_execution.py`, `tests/test_modbus.py`, `tests/test_mqtt_adapter.py`, `tests/test_reflex.py`, `tests/test_simulation.py`, `tests/test_verification.py`, `tests/test_zigbee2mqtt.py` → [tests de jabfy-bus](tests.md)
