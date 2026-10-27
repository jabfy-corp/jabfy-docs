# Veille

> Objectif obligatoire 1 : *Track what's out there and use it to crack your project's hard problem.*

Le problème dur de Jabfy : **un assistant vocal qui comprend le français et agit sur la maison, sans jamais rien envoyer dans le cloud, et sans que l'IA puisse faire une action dangereuse**. Il se décompose en six questions, une fiche chacune.

## Synthèse

| Domaine | Fiche | Choix | Statut |
|---|---|---|---|
| Mot d'activation | [Wake word](wake-word.md) | openWakeWord, avec un modèle « Jabfy » entraîné par l'équipe | Proposé |
| Voix → texte | [STT](stt.md) | faster-whisper ; taille du modèle à trancher sur mesure | Confirmé ([ADR-0008](../architecture/adr/0008-faster-whisper.md)) |
| Compréhension et proposition | [LLM local](llm-local.md) | Ollama ou llama.cpp via une API compatible OpenAI ; modèle d'environ 8B à confirmer | Moteur confirmé, modèle **mesuré** |
| Texte → voix | [TTS](tts.md) | Kokoro-82M via jabfy-tts | Confirmé ([ADR-0009](../architecture/adr/0009-kokoro-tts.md)) |
| Appareils de la maison | [Protocoles domotiques](protocoles-domotiques.md) | MQTT et Zigbee2MQTT d'abord, Matter ensuite | Appliqué ([ADR-0005](../architecture/adr/0005-mqtt-zigbee2mqtt.md)) |
| Données personnelles | [Vie privée](vie-privee.md) | Tout en local, minimisation, audit des actions | Appliqué, preuves à produire |

## Ce que la veille a changé dans le projet

- **Les mesures sur le modèle de langage** ont montré qu'un modèle de 3 milliards de paramètres peut agir sur une question hors sujet : elles justifient de brancher jabfy-guard sur Core, et orientent vers un modèle d'environ 8 milliards de paramètres ([Intentions](../performance/intentions.md)).
- **Les licences** ont écarté plusieurs solutions populaires : les modèles pré-entraînés d'openWakeWord et XTTS-v2 sont non commerciaux, Piper est passé en GPL-3.0.
- **Les sorties structurées** des moteurs locaux permettent de garantir un JSON valide, sans dépendre du bon vouloir du modèle.
- **Le marché va vers plus de cloud** (Amazon a supprimé le traitement local d'Alexa en mars 2025), ce qui renforce le positionnement 100 % local de Jabfy.

## Méthode

Chaque fiche suit le même [modèle](modele.md) : le problème, les solutions existantes, un tableau comparatif, le choix retenu et pourquoi les autres sont écartés, les avancées récentes, les sources.

Toutes les fiches comparent les solutions sur les mêmes critères :

| Critère | Ce qu'on note |
|---|---|
| 100 % local | Fonctionne sans aucun appel réseau sortant, une fois installé |
| Latence | Mesurée par Jabfy quand c'est possible, sinon ordre de grandeur publié |
| Qualité en français | Score mesuré (WER, taux de bonne action…) ou appréciation argumentée |
| RAM | Empreinte mémoire en fonctionnement |
| Licence | Licence du code **et** licence des modèles, qui sont souvent différentes |

Une fiche peut ajouter des critères propres à son domaine (par exemple la sécurité native pour les protocoles), mais ne retire jamais les critères communs. Une décision issue de la veille est consignée dans un [ADR](../architecture/adr/README.md).

Règles :

- dater chaque mesure et noter la version testée ;
- citer ses sources avec un lien, et signaler les sources tierces ;
- préférer une mesure faite par nous à un chiffre annoncé par un éditeur ;
- vérifier la licence des **poids** d'un modèle, pas seulement celle du code.
