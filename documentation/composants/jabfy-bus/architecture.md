# Architecture — JABFY Universal JSON Bus

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/architecture.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/architecture.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Vue d'ensemble

```text
Data Ingestion Layer
        ↓
Protocol Adapters        (jabfy_bus/adapters)
        ↓
Universal JSON Bus       (jabfy_bus/core)
        ↓
Reasoning Engine         (externe, publie command.requested)
        ↓
Verification Engine      (jabfy_bus/verification)
        ↓
Execution Layer          (jabfy_bus/execution)
        ↓
Audit Logs               (jabfy_bus/audit)
```

## Règles architecturales

1. **Aucun protocole externe ne dicte le modèle interne.** Chaque
   adapter traduit son protocole vers le vocabulaire commun
   (`core/types.py`) : domaines, classes sémantiques, actions.
2. **La normalisation ne supprime jamais l'information brute.**
   Chaque `BusMessage` porte `source.raw_address`, `value.raw` et le
   payload complet dans `raw`.
3. **Toute commande passe par le Verification Engine.** Le pipeline
   `command.requested → command.approved|rejected → command.executed`
   est le seul chemin d'exécution. L'Execution Layer refuse tout
   message d'approbation ne venant pas du Verification Engine
   (`VerificationBypass`).
4. **Chaque décision est traçable.** L'audit est append-only, avec
   chaînage de hash SHA-256 : toute altération casse la chaîne.
5. **Une approbation n'est valable qu'une fois.** Avec
   `approval_validator=engine.consume_approval`, l'Execution Layer
   n'accepte que la commande exacte approuvée, une seule fois, pendant
   son dispatch synchrone (voir `security.md`).
6. **Read-only par défaut.** Un adapter doit être explicitement
   configuré `read_write`, et côté Modbus chaque registre doit en
   plus opter pour l'écriture (`write_allowed`).

## Flux d'un message

```text
MQTT topic "zigbee2mqtt/salon_motion" {"occupancy": true}
   ↓ Zigbee2MQTTAdapter.handle_mqtt()
BusMessage(telemetry, entity=binary_sensor.salon_motion, value=true, raw={...})
   ↓ bus.publish()
EntityRegistry (dernier état) + Reasoning (règles) + WebSocket stream
   ↓ Reasoning publie command.requested(turn_on, switch.salon_lamp)
VerificationEngine.review() → policy "home_light_low_risk_v1" → approved
   ↓ command.approved (correlation_id = message_id de la requête)
ExecutionLayer.execute() → translate("mqtt", command) → transport MQTT
   ↓ command.executed + AuditLog.append()
```

## Modules

| Module | Rôle |
|---|---|
| `core` | Modèle de message, bus pub/sub, registre d'entités |
| `adapters` | MQTT, HTTP (polling + webhooks), Zigbee2MQTT, Modbus TCP, CoAP (P2) |
| `verification` | Classification de risque, policies déclaratives, engine |
| `execution` | Traducteurs par protocole, transports, exécution |
| `audit` | Journal append-only à chaînage de hash |
| `simulation` | Devices simulés, lab, scénarios de démo |
| `api` | Consultation HTTP + flux WebSocket (lecture seule) |

## Intégration V0.0.1 (maison virtuelle)

Le bus est embarqué par `jabfy-simulation`, qui lui injecte :

- un `authorizer` (Guard) dans `VerificationEngine`, à la place des
  policies historiques ;
- un `AuditLog` écrit avant dispatch ;
- `approval_validator=engine.consume_approval` dans `ExecutionLayer`.

`jabfy-deploy` orchestre la pile locale. Le mode autonome (policies +
`jabfy-bus demo`) reste disponible et inchangé. Exemple de code dans
`interfaces.md`.

## Priorités protocolaires

Voir l'audit complet dans `audit_protocoles_iot_jabfy_universal_json_bus.md`.

- **P0** : MQTT, HTTP REST, Zigbee via Zigbee2MQTT, WebSocket interne
- **P1** : Matter, Modbus TCP, OPC UA (read/subscribe)
- **P2** : Z-Wave (via Z-Wave JS), BACnet, KNX, CoAP, BLE
- **P3/P4** : LoRaWAN, LwM2M, DDS
