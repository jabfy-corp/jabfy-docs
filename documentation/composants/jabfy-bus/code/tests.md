# jabfy-bus — tests

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/tests.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/tests.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

Total : **96 tests** répartis dans 11 fichiers (comptés par `def test_`).

| fichier | tests | code importé |
|---|---|---|
| `tests/test_admission.py` | 7 | [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/verification/engine.py](verification-engine.md), [jabfy_bus/verification/policies.py](verification-policies.md) |
| `tests/test_api.py` | 5 | [jabfy_bus/api/app.py](api-app.md), [jabfy_bus/api/ws.py](api-ws.md), [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/registry.py](core-registry.md), [jabfy_bus/core/types.py](core-types.md) |
| `tests/test_audit.py` | 7 | [jabfy_bus/audit/log.py](audit-log.md) |
| `tests/test_bus.py` | 9 | [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md) |
| `tests/test_execution.py` | 9 | [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/execution/translators.py](execution-translators.md), [jabfy_bus/verification/engine.py](verification-engine.md), [jabfy_bus/verification/policies.py](verification-policies.md) |
| `tests/test_message.py` | 12 | [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md) |
| `tests/test_modbus.py` | 9 | [jabfy_bus/adapters/modbus/adapter.py](modbus-adapter.md), [jabfy_bus/adapters/modbus/registers.py](modbus-registers.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/types.py](core-types.md) |
| `tests/test_mqtt_adapter.py` | 11 | [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md), [jabfy_bus/adapters/mqtt/mapping.py](mqtt-mapping.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/types.py](core-types.md) |
| `tests/test_simulation.py` | 6 | [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/simulation/devices.py](simulation-devices.md), [jabfy_bus/simulation/lab.py](simulation-lab.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md) |
| `tests/test_verification.py` | 15 | [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/types.py](core-types.md), [jabfy_bus/verification/engine.py](verification-engine.md), [jabfy_bus/verification/policies.py](verification-policies.md), [jabfy_bus/verification/risk.py](verification-risk.md) |
| `tests/test_zigbee2mqtt.py` | 6 | [jabfy_bus/adapters/zigbee2mqtt/adapter.py](zigbee2mqtt-adapter.md), [jabfy_bus/core/bus.py](core-bus.md) |

## À retenir

- `test_bus.py` couvre l'ordre de dispatch ; `test_execution.py` couvre `VerificationBypass` ; `test_audit.py` la chaîne de hachage.
- La CI teste Python 3.10 à 3.12 alors que Core exige 3.11 : sans conséquence, le bus reste compatible avec plus de versions que Core n'en demande.
