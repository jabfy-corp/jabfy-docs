# Wake word

| Statut                                                | Suivi par | Dernière mise à jour |
| ----------------------------------------------------- | --------- | -------------------- |
| Première version : choix proposé, à valider en équipe | Simeon    | 27/10/2026           |

## Le problème

Jabfy doit détecter en continu un mot d'activation (« Jabfy ») sur le micro, sans rien envoyer hors de la maison. C'est le seul composant qui écoute en permanence : il doit consommer très peu de CPU, réagir vite, et surtout se déclencher le moins possible par erreur (télévision, conversation). Le mot « Jabfy » n'existe dans aucun modèle prêt à l'emploi : il faudra entraîner un modèle sur mesure, si possible en français.

## Situation actuelle

[jabfy-voice](../../composants/composants.md) n'a pas de wake word : il commence à enregistrer dès que le volume dépasse un seuil, puis s'arrête après un silence. L'assistant réagit donc à tout son assez fort.

## Les solutions existantes

* **openWakeWord** — bibliothèque Python, utilisée par Home Assistant. Les modèles s'entraînent à partir de voix synthétiques, ce qui permet de créer un mot personnalisé sans enregistrer des centaines de locuteurs. Tourne sur CPU, y compris sur un Raspberry Pi.
* **microWakeWord** — moteur conçu pour ESPHome, qui tourne directement sur un microcontrôleur ESP32-S3. C'est lui qui équipe le micro-satellite Home Assistant Voice Preview Edition.
* **Porcupine (Picovoice)** — moteur commercial, très léger et précis, avec création de mots personnalisés en français depuis la console Picovoice.
* **Snowboy** — ancien moteur open source, abandonné : écarté d'office.

## Comparatif

| Solution                       | 100 % local                                                               | Latence                                 | Mot « Jabfy » en français          | Ressources            | Licence (code / modèle)                                                 |
| ------------------------------ | ------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------- | --------------------- | ----------------------------------------------------------------------- |
| openWakeWord                   | Oui                                                                       | Temps réel, par fenêtres audio de 80 ms | À entraîner sur voix synthétiques  | Faible, CPU           | Apache 2.0 / **modèles pré-entraînés CC BY-NC-SA 4.0 (non commercial)** |
| microWakeWord                  | Oui, sur le microcontrôleur                                               | Temps réel                              | À entraîner (outillage plus lourd) | Très faible, ESP32-S3 | Apache 2.0                                                              |
| Porcupine                      | Inférence locale, mais une clé liée à un compte Picovoice est obligatoire | Temps réel                              | Oui, via la console Picovoice      | Très faible           | SDK Apache 2.0, mots personnalisés soumis aux conditions du compte      |
| Détection par silence (actuel) | Oui                                                                       | Immédiate                               | Sans objet : pas de mot            | Quasi nulle           | Code Jabfy                                                              |

Mesure de référence : les faux déclenchements par heure, définis dans [Performance › Wake word](../../performance/wake-word.md).

## Choix proposé

**openWakeWord pour le prototype**, avec un modèle « Jabfy » entraîné par l'équipe :

* il s'intègre directement à jabfy-voice, en Python, sur la même machine ;
* l'entraînement par voix synthétiques permet de produire un modèle en français sans campagne d'enregistrement ;
* **les modèles pré-entraînés ne peuvent pas être utilisés commercialement** (CC BY-NC-SA 4.0). Il faut entraîner notre propre modèle et vérifier la licence des données d'entraînement utilisées, qui peut elle aussi être non commerciale.

**microWakeWord pour plus tard**, si Jabfy passe sur des satellites matériels dédiés (vision « nœuds basse consommation ») : il tourne sur un composant à quelques euros, sans ordinateur.

**Porcupine est écarté** : son fonctionnement dépend d'un compte chez un fournisseur, et les conditions de son offre gratuite sont contradictoires selon les sources (usage commercial autorisé ou non). C'est contraire au principe de souveraineté de Jabfy.

Ce choix sera consigné dans un ADR une fois validé.

## Avancées récentes

* Home Assistant a fait passer la détection du mot d'activation **sur l'appareil lui-même** (ESP32-S3) avec microWakeWord, ce qui évite d'envoyer le flux audio en continu vers un serveur.
* L'entraînement sur voix synthétiques, popularisé par openWakeWord, rend la création d'un mot personnalisé accessible à une petite équipe.

## Sources

* [openWakeWord — README et licence des modèles (Hugging Face)](https://huggingface.co/davidscripka/openwakeword/raw/main/README.md)
* [openWakeWord sur PyPI](https://pypi.org/project/openwakeword)
* [Home Assistant — Voice chapter 7 : microWakeWord, licence Apache 2.0](https://www.home-assistant.io/blog/2024/06/26/voice-chapter-7/)
* [Home Assistant — Voice chapter 6 : wake word sur ESP32-S3](https://www.home-assistant.io/blog/2024/02/21/voice-chapter-6/)
* [ESPHome — composant Micro Wake Word](https://esphome.io/components/micro_wake_word/)
* [Picovoice — Porcupine](https://picovoice.ai/platform/porcupine) et [tarifs](https://picovoice.ai/pricing)
* [Picovoice — présentation de l'offre gratuite (mise à jour janvier 2025)](https://picovoice.ai/blog/introducing-picovoices-free-tier)
