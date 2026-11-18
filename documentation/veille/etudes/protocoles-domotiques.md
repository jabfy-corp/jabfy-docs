# Protocoles domotiques

| Statut                                                            | Suivi par | Dernière mise à jour |
| ----------------------------------------------------------------- | --------- | -------------------- |
| Choix appliqué : MQTT et Zigbee2MQTT en production dans jabfy-bus | Elias     | 27/10/2026           |

## Le problème

Une maison mélange des appareils Zigbee, Wi-Fi, Matter, Z-Wave, parfois Modbus ou KNX. Jabfy doit tous les lire et les piloter **sans qu'aucun protocole ne dicte son modèle interne**, et sans perdre l'information d'origine (adresse, payload brut) utile au diagnostic et à l'audit. Chaque protocole ajouté est aussi une surface d'attaque : l'ordre d'intégration compte.

## Situation actuelle

[jabfy-bus](../../composants/composants.md) traduit chaque protocole vers un message JSON commun, le **bus JSON universel**, et fait vérifier toute commande avant de l'exécuter. Adapters disponibles : MQTT, Zigbee via Zigbee2MQTT, HTTP (interrogation et webhooks), Modbus TCP, et un squelette CoAP. La maison virtuelle de [jabfy-simulation](../../composants/composants.md) parle un vrai MQTT au format Zigbee2MQTT, du Modbus TCP et du HTTP, pour exercer ces adapters.

Cette fiche résume l'audit complet des protocoles réalisé pour le bus : [`audit_protocoles_iot_jabfy_universal_json_bus.md`](https://github.com/jabfy-corp/jabfy-bus/blob/main/audit_protocoles_iot_jabfy_universal_json_bus.md) (environ 1 900 lignes, 16 protocoles étudiés).

## Les solutions existantes

* **MQTT** — messagerie publication/abonnement légère, standard OASIS ; la lingua franca de la domotique libre.
* **Zigbee** — radio maillée basse consommation, la plus répandue pour capteurs, ampoules et prises. Exploitée via **Zigbee2MQTT**, qui la convertit en MQTT.
* **Matter** — standard unifié d'Apple, Google, Amazon et Samsung, sur Wi-Fi ou Thread. Stratégique à long terme.
* **Thread** — réseau maillé IP basse consommation, le transport radio de Matter.
* **Z-Wave** — radio sub-GHz fiable mais plus fermée, accessible via Z-Wave JS.
* **HTTP REST et WebSocket** — API locales des appareils Wi-Fi, webhooks, et flux temps réel internes.
* **Modbus TCP, OPC UA, BACnet, KNX** — protocoles industriels et du bâtiment : énergie, chauffage, GTB.
* **CoAP, LoRaWAN, LwM2M, BLE** — IoT contraint, longue portée, gestion de parc, présence.

## Comparatif

Les critères communs de la veille s'adaptent ici : la « qualité en français » est sans objet, et deux critères propres au domaine s'ajoutent, la sécurité native et le matériel nécessaire.

| Protocole               | 100 % local              | Latence     | Ressources | Licence / spécification                    | Sécurité native                                 | Matériel                  | Priorité Jabfy      |
| ----------------------- | ------------------------ | ----------- | ---------- | ------------------------------------------ | ----------------------------------------------- | ------------------------- | ------------------- |
| MQTT                    | Oui (broker local)       | Très faible | Minimes    | Standard OASIS ouvert                      | TLS et ACL à configurer, aucune par défaut      | Aucun                     | **P0**              |
| Zigbee via Zigbee2MQTT  | Oui                      | Faible      | Faibles    | Spécification CSA ; Zigbee2MQTT en GPL-3.0 | Chiffrement AES du réseau                       | Clé USB coordinateur      | **P0**              |
| HTTP REST / WebSocket   | Oui si API locale        | Faible      | Faibles    | Standards ouverts                          | Selon l'appareil, souvent faible                | Aucun                     | **P0**              |
| Matter (Wi-Fi / Thread) | Oui, conçu pour le local | Faible      | Moyennes   | Spécification CSA, SDK open source         | Forte : certificats, mise en service sécurisée  | Routeur de bordure Thread | P1                  |
| Modbus TCP              | Oui                      | Faible      | Minimes    | Spécification ouverte                      | **Aucune** (ni authentification ni chiffrement) | Équipements industriels   | P1 (lab industriel) |
| OPC UA                  | Oui                      | Faible      | Moyennes   | Standard ouvert (OPC Foundation)           | Forte                                           | Automates                 | P2                  |
| Z-Wave via Z-Wave JS    | Oui                      | Faible      | Faibles    | Spécification Z-Wave Alliance              | S2 (chiffrement)                                | Clé USB Z-Wave            | P2                  |
| BACnet / KNX            | Oui                      | Faible      | Faibles    | Standards du bâtiment                      | Variable, souvent faible                        | Passerelle IP             | P2                  |
| CoAP                    | Oui                      | Très faible | Minimes    | RFC 7252 (IETF)                            | DTLS optionnel                                  | Aucun                     | P2                  |
| LoRaWAN                 | Selon le serveur réseau  | Élevée      | Faibles    | LoRa Alliance                              | Chiffrement AES                                 | Passerelle LoRa           | P3                  |

## Choix retenu

**MQTT, Zigbee via Zigbee2MQTT et HTTP en priorité (P0)**, déjà implémentés dans jabfy-bus :

* MQTT est le plus simple et le plus universel, et c'est le langage commun de Zigbee2MQTT, de Home Assistant et de notre simulateur ;
* **Zigbee2MQTT plutôt que du Zigbee brut** : il gère la radio, la compatibilité de milliers d'appareils et l'inventaire ; le bus n'a plus qu'à consommer des topics MQTT ;
* HTTP couvre les appareils Wi-Fi qui exposent une API locale.

**Matter ensuite (P1)**, car c'est l'avenir de la maison connectée et il est conçu pour fonctionner en local, mais son intégration est plus lourde (mise en service, Thread). Un adapter expérimental existe sur une branche du bus.

**Modbus TCP** est déjà présent pour démontrer la crédibilité « bâtiment et énergie », avec une double autorisation d'écriture : ce protocole n'a aucune sécurité.

Écartés pour l'EIP : LoRaWAN, LwM2M, DDS (hors du périmètre maison), et l'intégration de Zigbee ou Z-Wave **en brut** (trop coûteuse face aux passerelles existantes).

## Avancées récentes

* **Matter 1.5** (novembre 2025) ajoute les caméras (sur WebRTC), les fermetures (volets, portails, portes de garage), la gestion de l'énergie (tarifs, intensité carbone du réseau) et le transport TCP. Samsung SmartThings l'a adopté dès décembre 2025.
* **Zigbee 4.0 et « Suzi »** (novembre 2025) : nouvelle version rétrocompatible avec Zigbee 3.0, avec des fréquences sub-GHz pour une meilleure portée, et une sécurité renforcée (agilité cryptographique).
* Ces deux évolutions confortent la stratégie : Zigbee reste pertinent via Zigbee2MQTT, et Matter couvre de plus en plus de types d'appareils.

## Sources

* [Audit des protocoles IoT pour le bus JSON universel (jabfy-bus)](https://github.com/jabfy-corp/jabfy-bus/blob/main/audit_protocoles_iot_jabfy_universal_json_bus.md)
* [OASIS — MQTT 5.0](https://www.oasis-open.org/standard/mqtt-v5-0-os/)
* [Connectivity Standards Alliance — Matter 1.5](https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/)
* [Connectivity Standards Alliance — Zigbee 4.0 et Suzi](https://csa-iot.org/newsroom/the-connectivity-standards-alliance-announces-zigbee-4-0-and-suzi-empowering-the-next-generation-of-secure-interoperable-iot-devices/)
* [CEPro — Matter 1.5 et adoption par SmartThings](https://www.cepro.com/news/connectivity-standards-alliance-releases-matter-1-5-adding-cameras-closures-and-new-energy-features/623552)
* [IETF RFC 7252 — CoAP](https://datatracker.ietf.org/doc/html/rfc7252)
* [Thread Group](https://threadgroup.org/), [Z-Wave Alliance](https://z-wavealliance.org/), [Modbus](https://www.modbus.org/modbus-specifications), [OPC Foundation](https://opcfoundation.org/about/opc-technologies/opc-ua/)
