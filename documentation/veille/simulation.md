# jabfy-simulation : une maison virtuelle qui se comporte comme du vrai matériel

| Responsables | Code | Mise à jour |
|---|---|---|
| Loan, Siméon | Python 3.11 et JavaScript ; V0.0.1 sur la branche `sim-2` | 18/11/2026 |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par les responsables.

## Le problème constaté

- **Tout le monde n'a pas des appareils Zigbee chez soi**, et une démo sur du vrai matériel n'est pas reproductible.
- **Tester une action dangereuse** (déverrouiller, ouvrir une vanne) sur un vrai appareil est risqué.
- **Une simulation « en mémoire » ne prouve rien** : il faut que le bus reçoive les mêmes messages que d'un vrai appareil.

## Les technologies et pourquoi

| Besoin | Choix | Pourquoi | Écarté |
|---|---|---|---|
| Appareils virtuels | Python, `paho-mqtt`, messages au format Zigbee2MQTT, broker Mosquitto | Les adapters du bus ne voient pas la différence avec du vrai matériel : on teste le vrai chemin | Faux appareils dans le code du bus : ne testent pas les adapters |
| Autres protocoles | Serveur Modbus (`pymodbus`) pour le chauffage, serveurs HTTP (FastAPI) pour la télé et le NAS | Couvrir les protocoles du bus avec les mêmes bibliothèques | — |
| Scène 3D | three.js, servi tel quel par le serveur Python | Bibliothèque 3D web la plus répandue ; tourne dans le navigateur sans étape de compilation | Babylon.js : complet mais plus lourd. Unity, Godot : application à installer, compilation |
| Plans et scénarios | YAML validé par Pydantic | Un plan de maison se lit et se modifie à la main, et se versionne dans Git | — |

**Pourquoi pas un simulateur existant ?** L'intégration « demo » de Home Assistant crée de faux appareils, mais à l'intérieur de Home Assistant, sans vrai protocole. Acheter un kit Zigbee par développeur coûte cher et ne passe pas en CI.

## Ce que la veille change

- **La CI est toujours rouge** : c'est un workflow Node sur un projet Python, donc aucune PR n'y est réellement testée. À remplacer par `pytest`.
- **La simulation embarque aujourd'hui le bus et Guard** (V0.0.1). Si le bus passe dans Core, elle redevient une simple maison virtuelle.

## Sources

- [Zigbee2MQTT : format des messages](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html)
- [Eclipse Mosquitto](https://mosquitto.org/)
- [three.js](https://threejs.org/), [Babylon.js](https://www.babylonjs.com/)
- [Home Assistant : intégration demo](https://www.home-assistant.io/integrations/demo/)
