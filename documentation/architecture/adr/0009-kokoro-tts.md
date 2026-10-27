# ADR-0009 — Kokoro-82M pour la synthèse vocale

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté (intégration avec jabfy-voice à décider) | 27/10/2026 | Eloi | [TTS](../../veille/tts.md) |

## Contexte

La réponse doit être lue à voix haute en français, sur la machine, avec une voix naturelle, et commencer avant la fin de la génération du texte. Deux solutions coexistaient : Kokoro-82M dans jabfy-tts, et pyttsx3 (eSpeak) dans jabfy-voice.

## Options étudiées

1. **Kokoro-82M** — petit modèle, voix naturelle, tourne sur CPU, poids sous Apache 2.0.
2. **Piper** — très rapide sur petit matériel, mais moteur passé en GPL-3.0 en 2025.
3. **pyttsx3 / eSpeak NG** — minuscule, mais voix robotique.
4. **XTTS-v2, Chatterbox** — plus naturels, mais licence non commerciale (XTTS) ou trop lourds sans GPU (Chatterbox).

## Décision

**Kokoro-82M**, porté par la bibliothèque jabfy-tts, avec synthèse phrase par phrase pour suivre la génération du modèle. pyttsx3 sera retiré de jabfy-voice.

## Conséquences

- Une seule voix française, de qualité moyenne : à surveiller, et à créditer (données SIWIS sous CC BY).
- jabfy-tts est en Rust et jabfy-voice en Python : il reste à choisir comment les relier, par la bibliothèque Python de Kokoro ou par jabfy-tts en service. Décision à consigner dans un prochain ADR.
- Les poids du modèle se téléchargent à part : ils ne sont pas embarqués dans la bibliothèque.
