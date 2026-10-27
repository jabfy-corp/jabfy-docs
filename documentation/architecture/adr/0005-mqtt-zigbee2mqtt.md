# ADR-0005 — MQTT et Zigbee2MQTT comme protocoles prioritaires

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté (consigné a posteriori) | 27/10/2026 | Elias | [Protocoles domotiques](../../veille/protocoles-domotiques.md) |

## Contexte

Le bus doit piloter des appareils hétérogènes, mais une petite équipe ne peut pas intégrer seize protocoles. L'audit des protocoles réalisé pour jabfy-bus en a classé seize par pertinence, facilité et risque. Zigbee est le protocole radio le plus répandu en domotique, mais son intégration directe (radio, clusters, appairage) est longue.

## Options étudiées

1. **MQTT + Zigbee via Zigbee2MQTT + HTTP** — Zigbee2MQTT gère la radio et des milliers d'appareils, et publie tout en MQTT ; le bus n'a plus qu'un protocole simple à consommer.
2. **Zigbee en direct** (pile radio dans le bus) — aucun intermédiaire, mais des mois de travail pour un résultat moins compatible.
3. **Matter d'abord** — le standard d'avenir, mais une intégration plus lourde (mise en service, Thread) et un parc d'appareils encore partiel.

## Décision

Priorité **P0** à **MQTT, Zigbee via Zigbee2MQTT et HTTP**. **Matter en P1**, une fois la base stable. Modbus TCP est ajouté pour démontrer la crédibilité « bâtiment et énergie ».

## Conséquences

- Le simulateur parle le même format que Zigbee2MQTT (`zigbee2mqtt/<id>` et `zigbee2mqtt/<id>/set`) : les adapters sont testés comme sur du vrai matériel.
- Le bus dépend de Zigbee2MQTT pour le Zigbee : une clé USB coordinateur et ce service sont nécessaires sur une vraie installation.
- MQTT n'ayant aucune sécurité par défaut, TLS et ACL sont obligatoires en production, et les messages conservés (« retained ») sont surveillés, car une vieille commande pourrait être rejouée.
