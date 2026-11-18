# jabfy-voice

| Responsable | Code            | Mise à jour |
| ----------- | --------------- | ----------- |
| Elias       | Python ; `main` | 18/11/2026  |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par le responsable.

## Le problème constaté

* **Comprendre le français parlé, sur la machine**, assez vite pour une conversation.
* **Savoir quand l'utilisateur parle à Jabfy** : aujourd'hui, l'écoute est permanente et il n'y a pas de mot d'activation.
* **Savoir quand il a fini de parler** : aujourd'hui, un seuil de volume fixe. Un bruit de fond prolonge l'écoute, une voix faible la coupe.

## Les technologies et pourquoi

| Besoin           | Choix                                                                                          | Pourquoi                                                                                                                              | Écarté                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Voix vers texte  | faster-whisper, modèle `base` sur CPU ([ADR-0008](../architecture/adr/0008-faster-whisper.md)) | Whisper est le meilleur modèle libre en français ; cette version est jusqu'à 4 fois plus rapide que l'originale, pour la même qualité | Vosk : léger mais moins précis. Whisper original : plus lent. API cloud : contraire au 100 % local        |
| Micro            | PyAudio                                                                                        | Simple, multiplateforme                                                                                                               | —                                                                                                         |
| Fin de parole    | Volume moyen comparé à un seuil fixe                                                           | Rapide à écrire pour un prototype                                                                                                     | Voir « Ce que la veille change »                                                                          |
| Mot d'activation | Aucun pour l'instant                                                                           | —                                                                                                                                     | Proposé : openWakeWord, avec un modèle « Jabfy » entraîné par l'équipe ([Wake word](etudes/wake-word.md)) |
| Réponse vocale   | pyttsx3 (eSpeak NG sous Linux)                                                                 | Aucun modèle à télécharger                                                                                                            | À remplacer par Kokoro via jabfy-tts ([ADR-0009](../architecture/adr/0009-kokoro-tts.md))                 |
| Interface web    | Flask                                                                                          | Une page de test, vite écrite                                                                                                         | Les autres API Python sont en FastAPI ([ADR-0002](../architecture/adr/0002-fastapi.md)) : à aligner       |

## Ce que la veille change

* **Détection de la parole** : faster-whisper intègre le modèle Silero VAD (option `vad_filter`). Il distingue la voix du bruit, au lieu d'un seuil de volume.
* **Le code ne tournera pas sous Python 3.13** : il utilise le module `audioop`, supprimé de la bibliothèque standard en 3.13 (PEP 594).
* **La voix appelle Ollama directement** (modèle `llama3.2`) et ne peut donc pas agir sur la maison. Dans la direction « orchestrateur », elle devient un spécialiste appelé par Core, et toute action repasse par Guard et le bus.
* **La taille du modèle Whisper reste à choisir sur mesure** : taux d'erreur en français contre temps de réponse ([STT](etudes/stt.md)).

## Sources

* [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [Silero VAD](https://github.com/snakers4/silero-vad)
* [PEP 594 : suppression de modules dont `audioop`](https://peps.python.org/pep-0594/)
* Études détaillées : [STT](etudes/stt.md), [Wake word](etudes/wake-word.md)
