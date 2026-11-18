# Études par domaine

Les sujets qui demandent une comparaison détaillée, avec mesures, ont leur propre étude. Les [fiches projet](../veille/#par-projet) y renvoient.

Chaque étude compare les solutions sur les mêmes critères : **100 % local**, **latence**, **qualité en français**, **RAM** et **licence** (du code et des poids du modèle, souvent différentes).

| Domaine                                           | Utilisé par     | Choix                                                        | Statut                                                                 |
| ------------------------------------------------- | --------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------- |
| [Wake word](wake-word.md)                         | voice           | openWakeWord, avec un modèle « Jabfy » entraîné par l'équipe | Proposé                                                                |
| [STT](stt.md)                                     | voice           | faster-whisper ; taille du modèle à trancher sur mesure      | Confirmé ([ADR-0008](../../architecture/adr/0008-faster-whisper.md))   |
| [LLM local](llm-local.md)                         | core            | Ollama ou llama.cpp ; modèle d'environ 8B à confirmer        | Moteur confirmé, modèle **mesuré**                                     |
| [TTS](tts.md)                                     | tts, voice      | Kokoro-82M                                                   | Confirmé ([ADR-0009](../../architecture/adr/0009-kokoro-tts.md))       |
| [Protocoles domotiques](protocoles-domotiques.md) | bus, simulation | MQTT et Zigbee2MQTT d'abord, Matter ensuite                  | Appliqué ([ADR-0005](../../architecture/adr/0005-mqtt-zigbee2mqtt.md)) |
| [Vie privée](vie-privee.md)                       | tous            | Tout en local, minimisation, audit des actions               | Appliqué, preuves à produire                                           |
