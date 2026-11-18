# Synthèse et méthode

> Objectif obligatoire 1 : _Track what's out there and use it to crack your project's hard problem._

Le problème dur de Jabfy : **un assistant vocal qui comprend le français et agit sur la maison, sans jamais rien envoyer dans le cloud, et sans que l'IA puisse faire une action dangereuse**.

La veille répond, pour chaque projet qui contient du code, à trois questions : **quel problème on constate**, **quelle technologie on utilise**, et **pourquoi celle-là plutôt qu'une autre**.

## Par projet

| Projet                               | Problème constaté                                                                 | Choix principal                                              | Point ouvert                                              |
| ------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| [jabfy-core](../core.md)             | Le modèle peut agir sur une question hors sujet, ou renvoyer un JSON invalide     | Ollama derrière une API compatible OpenAI, sorties vérifiées | Choix du modèle ; contrat d'API                           |
| [jabfy-bus](../bus.md)               | Un protocole par appareil ; l'IA ne doit rien exécuter sans autorisation ni trace | Message JSON commun, adapters par protocole, audit chaîné    | Fuite de mémoire de la déduplication                      |
| [jabfy-guard](../guard.md)           | Une action non demandée ou piégée peut être dangereuse                            | Règles déterministes, refus par défaut, risque par action    | Pas encore sur `main` ; comparer avec un modèle fine-tuné |
| [jabfy-simulation](../simulation.md) | Pas de matériel pour tout le monde, tests risqués sur du vrai matériel            | Appareils virtuels qui parlent un vrai MQTT, scène three.js  | CI rouge                                                  |
| [jabfy-voice](../voice.md)           | Transcrire le français en local ; savoir quand on lui parle                       | faster-whisper                                               | Pas de mot d'activation ; incompatible avec Python 3.13   |
| [jabfy-tts](../tts.md)               | Voix naturelle sans GPU, qui parle avant la fin de la réponse                     | Kokoro-82M en Rust, phrase par phrase                        | Dépend d'un fork non fusionné                             |
| [jabfy-deploy](../deploy.md)         | Quatre applications à assembler, « ça marche chez moi »                           | Docker Compose, versions figées par commit                   | Tests de déploiement en CI                                |
| [jabfy-desktop](../desktop.md)       | Une interface sans logique de décision, pour une petite équipe                    | Electron, React, TypeScript                                  | Réévaluer Tauri, plus léger                               |
| [jabfy-website](../website.md)       | Présenter le projet, recueillir des contacts                                      | React, Tailwind, Express                                     | Versions non figées ; RGPD des formulaires                |

Pas de fiche pour les repos sans code : **jabfy-web** et **jabfy-mobile** (README seulement). **jabfy-prototype**, le premier prototype (Electron, React, FastAPI et Ollama), a été remplacé par Core, la simulation et desktop ; ses choix sont repris dans leurs fiches.

## Études par domaine

Six sujets demandent une comparaison détaillée, avec mesures : wake word, STT, LLM local, TTS, protocoles domotiques et vie privée. Voir les [études par domaine](../etudes/).

## Ce que la veille a changé dans le projet

* **Guard devient prioritaire.** Un modèle de 3 milliards de paramètres a agi sur une question hors sujet, et le vérificateur actuel de Core l'aurait laissé passer ([Intentions](../../performance/intentions.md)).
* **La mesure du bus a trouvé une fuite de mémoire**, à corriger avant toute démo de longue durée ([Performance du bus](../../performance/bus.md)).
* **Les licences ont écarté des solutions populaires** : les modèles pré-entraînés d'openWakeWord et XTTS-v2 sont non commerciaux, Piper est passé en GPL-3.0.
* **Trois risques de maintenance repérés** : jabfy-tts dépend d'un fork non fusionné, jabfy-voice utilise un module supprimé de Python 3.13, jabfy-website ne fige aucune version.
* **Le marché va vers plus de cloud** (Amazon a supprimé le traitement local d'Alexa en mars 2025), ce qui renforce le positionnement 100 % local de Jabfy.

## Méthode

Chaque fiche projet suit le même [modèle](modele.md) : le problème constaté, un tableau « besoin, choix, pourquoi, écarté », ce que la veille change, les sources. Une fiche tient sur un écran ; le détail va dans une étude par domaine.

Règles :

* dater chaque mesure et noter la version testée ;
* citer ses sources avec un lien ;
* préférer une mesure faite par nous à un chiffre annoncé par un éditeur ;
* une raison reconstituée après coup est signalée comme telle, et confirmée par le responsable du repo ;
* une décision qui engage plusieurs repos est consignée dans un [ADR](../../architecture/adr/).
