# Roadmap technique

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/roadmap.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/roadmap.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Phase 1 — Base solide ✅

Pipeline complet, démontrable, propre :

- [x] Modèle de message v1.0 + validation + JSON Schema
- [x] Bus pub/sub interne (dédup, historique, isolation des handlers)
- [x] MQTT Adapter (mapping déclaratif, client injectable)
- [x] HTTP Adapter (polling + webhooks)
- [x] Verification Engine minimal (risque + policies + default deny)
- [x] Execution Layer (traducteurs mqtt/http/modbus/simulation)
- [x] Audit append-only à chaînage de hash
- [x] Simulation Lab + scénario motion → light

Démo : `jabfy-bus demo --steps 10`

## Phase 1bis — Intégration V0.0.1 ✅

Fusionnée sur `main` le 26/10/2026 (PR #6).

- [x] `authorizer` externe (Guard) dans le Verification Engine
- [x] Audit écrit avant dispatch (`fsync`), refus si chaîne corrompue
- [x] Admission à usage unique (`consume_approval`)
- [x] Type de message `user_situation` (consigne utilisateur venant de Core)
- [x] Origines autorisées pour l'API (CORS, WebSocket)
- [x] Actions `set_position`, `set_tilt`, `set_mode`
- [x] Publication de l'image conteneur (`ghcr.io/jabfy-corp/jabfy-bus`) à chaque push sur `main`

## Phase 2 — Domotique sérieuse

- [x] Zigbee2MQTT deep mapping (exposes, inventaire bridge)
- [ ] Home Assistant bridge
- [ ] Matter adapter expérimental
- [x] WebSocket event stream (`/bus/events`, `/verification/decisions`, `/audit/live`)
- [ ] Capability discovery automatique

## Phase 3 — Industriel / bâtiment

- [x] Modbus TCP adapter (register map sémantique)
- [ ] OPC UA read/subscribe adapter
- [ ] BACnet adapter
- [ ] KNX IP adapter
- [ ] Risk policies avancées (validation humaine pour high/critical) — le refus par Guard est déjà en place, pas la validation humaine

## Phase 4 — IoT étendu

- [ ] LoRaWAN application adapter
- [ ] LwM2M adapter
- [ ] BLE adapter (présence, capteurs)
- [ ] Device lifecycle management
