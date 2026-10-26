# `jabfy_bus/core/message.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/core-message.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/core-message.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — L'enveloppe JSON commune : `BusMessage` (type, source, entité, trust, risque, `correlation_id`…).

Dépôt : [jabfy-bus](README.md) · 199 lignes · statut : **actif**

Docstring du module : *Modèle de message normalisé du bus JABFY (schéma v1.0).*

## À retenir

- `BusMessage` l.76, `validate` l.93, fabrique `new_message` l.169.
- Schéma publié : `schemas/bus-message-1.0.json`.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 20 | `_utcnow()` |  |
| 25 | classe `Source` | Provenance du message. `raw_address` garde l'adresse native |
| 38 | classe `Entity` | Identité logique normalisée de l'entité concernée. |
| 50 | classe `Value` | Valeur mesurée : brute et normalisée, jamais l'une sans l'autre. |
| 61 | classe `Quality` |  |
| 68 | classe `Security` |  |
| 76 | classe `BusMessage` | Message universel du bus, schéma v1.0. — méthodes : `validate` 93, `to_dict` 135, `from_dict` 143 |
| 169 | `new_message()` | Fabrique un message validé prêt à publier sur le bus. |

## Relations

- **Utilise** : [jabfy_bus/core/errors.py](core-errors.md), [jabfy_bus/core/types.py](core-types.md)
- **Utilisé par** : [jabfy_bus/adapters/base.py](base.md), [jabfy_bus/adapters/coap/adapter.py](coap-adapter.md), [jabfy_bus/adapters/http/adapter.py](http-adapter.md), [jabfy_bus/adapters/http/webhook.py](http-webhook.md), [jabfy_bus/adapters/modbus/adapter.py](modbus-adapter.md), [jabfy_bus/adapters/mqtt/adapter.py](mqtt-adapter.md), [jabfy_bus/adapters/zigbee2mqtt/adapter.py](zigbee2mqtt-adapter.md), [jabfy_bus/api/ws.py](api-ws.md), [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/cli.py](cli.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/registry.py](core-registry.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/simulation/lab.py](simulation-lab.md), [jabfy_bus/simulation/scenarios.py](simulation-scenarios.md), [jabfy_bus/verification/engine.py](verification-engine.md), [jabfy_bus/verification/policies.py](verification-policies.md), [jabfy_bus/verification/risk.py](verification-risk.md), app/api/routes_bus.py (jabfy-core), app/core/action_orchestrator.py (jabfy-core), app/core/guard.py (jabfy-core), app/core/run_journal.py (jabfy-core), sim/dashboard/commands.py (jabfy-simulation), sim/integration/reflex.py (jabfy-simulation)
- **Testé par** : `tests/test_admission.py`, `tests/test_api.py`, `tests/test_bus.py`, `tests/test_bus_http_modbus.py`, `tests/test_dashboard.py`, `tests/test_execution.py`, `tests/test_guard.py`, `tests/test_headless.py`, `tests/test_message.py`, `tests/test_reflex.py`, `tests/test_verification.py` → [tests de jabfy-bus](tests.md)
