# `jabfy_bus/simulation/scenarios.py`

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/simulation-scenarios.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/simulation-scenarios.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

> **Rôle** — Scénario de démo autonome du bus : capteur de mouvement → règle → lumière.

Dépôt : [jabfy-bus](README.md) · 150 lignes · statut : **actif**

Docstring du module : *Scénarios de démonstration du pipeline complet.*

## À retenir

- `MotionLightRule` l.49 : remplaçant simplifié du raisonnement (adapter `reasoning_stub`).
- `build_demo_stack` l.95, `run_motion_light_demo` l.143.

## Contenu (ligne → élément)

| ligne | élément | note |
|---|---|---|
| 36 | classe `DemoStack` | Pipeline complet câblé, prêt à tourner. |
| 49 | classe `MotionLightRule` | Raisonnement minimal : mouvement détecté -> proposer d'allumer la lampe. — méthodes : `__init__` 56, `attach` 62, `on_message` 66 |
| 95 | `build_demo_stack()` | Câble le pipeline complet du scénario motion -> light. |
| 143 | `run_motion_light_demo()` | Fait tourner le scénario : mouvement forcé au 3e tick. |

## Relations

- **Utilise** : [jabfy_bus/audit/log.py](audit-log.md), [jabfy_bus/core/bus.py](core-bus.md), [jabfy_bus/core/message.py](core-message.md), [jabfy_bus/core/registry.py](core-registry.md), [jabfy_bus/core/types.py](core-types.md), [jabfy_bus/execution/executor.py](execution-executor.md), [jabfy_bus/simulation/devices.py](simulation-devices.md), [jabfy_bus/simulation/lab.py](simulation-lab.md), [jabfy_bus/verification/engine.py](verification-engine.md), [jabfy_bus/verification/policies.py](verification-policies.md)
- **Utilisé par** : [examples/demo_pipeline.py](examples-demo-pipeline.md), [jabfy_bus/cli.py](cli.md)
- **Testé par** : `tests/test_simulation.py` → [tests de jabfy-bus](tests.md)
