# ADR-0008 — faster-whisper pour la reconnaissance vocale

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté (taille du modèle à trancher sur mesure) | 27/10/2026 | Elias | [STT](../../veille/stt.md) |

## Contexte

La voix doit être transcrite en français, localement, sur une machine sans GPU. jabfy-voice utilise déjà faster-whisper avec le modèle `base`.

## Options étudiées

1. **faster-whisper** — Whisper réimplémenté sur CTranslate2 : même précision, jusqu'à 4 fois plus rapide, quantification `int8`, licence MIT.
2. **Vosk** — très léger et en flux, mais nettement moins précis en français.
3. **Parakeet (NVIDIA) ou Voxtral (Mistral)** — très bons, mais pensés pour un GPU.

## Décision

**faster-whisper** est retenu comme moteur. La taille du modèle (`base` ou `small`) sera choisie d'après la mesure du taux d'erreur sur notre jeu de phrases ([Performance › WER](../../performance/stt-wer.md)).

## Conséquences

- Fonctionne sur CPU, sans service en ligne après le premier téléchargement du modèle.
- Le passage de `base` à `small` améliorera la précision au prix de la latence et de la mémoire (environ 2 Go) : à arbitrer avec la machine cible.
- Parakeet et Voxtral restent en veille si la cible dispose d'un GPU.
