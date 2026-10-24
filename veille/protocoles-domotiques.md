# Protocoles domotiques

| Statut | Responsable | Dernière mise à jour |
|---|---|---|
| Audit existant à reprendre | | |

## Le problème

Piloter des appareils hétérogènes (Zigbee, MQTT, Modbus, HTTP…) sans laisser aucun protocole dicter le modèle interne de Jabfy, et sans perdre la donnée brute.

## Situation actuelle

- [jabfy-bus](https://github.com/jabfy-corp/jabfy-bus) traduit chaque protocole vers un message JSON commun. Adapters existants : MQTT, HTTP, Zigbee2MQTT, Modbus TCP, CoAP.
- Un audit complet des protocoles existe déjà : [`audit_protocoles_iot_jabfy_universal_json_bus.md`](https://github.com/jabfy-corp/jabfy-bus/blob/main/audit_protocoles_iot_jabfy_universal_json_bus.md) (repo privé). Cette fiche doit en reprendre la synthèse au format commun.
- Prévus dans la roadmap du bus : Matter, pont Home Assistant, OPC UA, BACnet.

## Critères

Critères fixes, plus deux critères propres au domaine :

| Protocole | 100 % local | Latence | Qualité en français | RAM | Licence / spec ouverte | Sécurité native | Matériel nécessaire |
|---|---|---|---|---|---|---|---|
| MQTT | | | sans objet | | | | |
| Zigbee (via Zigbee2MQTT) | | | sans objet | | | | |
| Modbus TCP | | | sans objet | | | | |
| HTTP | | | sans objet | | | | |
| CoAP | | | sans objet | | | | |
| Matter | | | sans objet | | | | |

## Choix retenu

## Avancées récentes

## Sources
