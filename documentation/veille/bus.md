# jabfy-bus

| Responsables | Code                                                     | Mise à jour |
| ------------ | -------------------------------------------------------- | ----------- |
| Elias, Joan  | Python 3.10+ ; V0.0.1 fusionnée sur `main` le 26/10/2026 | 18/11/2026  |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par les responsables.

## Le problème constaté

* **Chaque appareil parle son propre protocole** : MQTT, Zigbee, HTTP, Modbus, CoAP. Sans couche commune, Core devrait connaître chacun d'eux.
* **L'IA ne doit jamais piloter un appareil directement.** Toute commande doit être autorisée, une seule fois, et tracée avant d'être envoyée.
* **Il faut pouvoir prouver après coup ce qui a été fait**, et détecter une trace modifiée.

## Les technologies et pourquoi

| Besoin                  | Choix                                                                                                    | Pourquoi                                                                                                                                                                    | Écarté                                                                                                         |
| ----------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Langage                 | Python                                                                                                   | Même langage que Core, Guard et la simulation : le bus s'embarque comme bibliothèque, sans service de plus ([ADR-0006](../architecture/adr/0006-bus-et-guard-embarques.md)) | Go ou Rust : plus rapides, mais une pile de plus, alors que nos mesures donnent 0,65 ms par commande en Python |
| Format commun           | Message JSON v1.0, décrit par un schéma JSON                                                             | Lisible, débogable à l'œil, compris par tous les langages de l'équipe                                                                                                       | Protobuf, CBOR : plus compacts, mais inutiles à ce débit et illisibles sans outil                              |
| Protocoles prioritaires | MQTT avec `paho-mqtt`, Zigbee via Zigbee2MQTT ([ADR-0005](../architecture/adr/0005-mqtt-zigbee2mqtt.md)) | Zigbee2MQTT gère la radio et des milliers d'appareils : le bus ne lit que des messages MQTT                                                                                 | Zigbee brut : trop coûteux face aux passerelles existantes                                                     |
| Bâtiment et énergie     | Modbus TCP avec `pymodbus`                                                                               | Montre que le bus va au-delà de la maison. Le protocole n'a aucune sécurité, d'où une double autorisation d'écriture                                                        | —                                                                                                              |
| Audit                   | Journal en ajout seul, chaîné en SHA-256, écrit avant l'envoi                                            | Toute modification casse la chaîne ; sans dépendance                                                                                                                        | Base de données dédiée (immudb…) : un service de plus pour un besoin simple                                    |
| Suivi en direct         | FastAPI et WebSocket (optionnels)                                                                        | Même outil que les autres API Python ([ADR-0002](../architecture/adr/0002-fastapi.md))                                                                                      | —                                                                                                              |

**Pourquoi pas Home Assistant comme bus ?** Home Assistant sait déjà parler à des milliers d'appareils, et son intégration Ollama permet à un modèle local de les commander. Mais la sécurité y repose surtout sur le choix des appareils exposés au modèle, sans règles par commande, limites de fréquence ni audit chaîné comparables à Guard et au bus. C'est ce que Jabfy apporte. Une passerelle vers Home Assistant est explorée sur une branche du bus, pour en réutiliser les intégrations.

## Ce que la veille change

* **La mesure a trouvé une fuite de mémoire.** Pour ignorer les doublons, le bus garde l'identifiant de chaque message, sans jamais le purger : environ 10 Mo par jour à un message par seconde ([Performance du bus](../performance/bus.md)). Correction : limiter la mémoire des doublons à une fenêtre (nombre de messages ou durée).
* **Matter est l'étape suivante**, car il est conçu pour fonctionner en local. Un adapter expérimental existe sur une branche, comme OPC UA et la présence Bluetooth.

## Sources

* [Zigbee2MQTT](https://www.zigbee2mqtt.io/)
* [paho-mqtt](https://pypi.org/project/paho-mqtt/), [pymodbus](https://github.com/pymodbus-dev/pymodbus)
* [Home Assistant : intégration Ollama et appareils exposés](https://www.home-assistant.io/integrations/ollama/)
* Étude détaillée : [Protocoles domotiques](etudes/protocoles-domotiques.md)
