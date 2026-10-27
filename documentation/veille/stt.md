# Reconnaissance vocale (STT)

| Statut | Suivi par | Dernière mise à jour |
|---|---|---|
| Première version : choix confirmé, mesure de WER à faire | Elias | 27/10/2026 |

## Le problème

Transcrire en texte une demande orale en français, sur la machine, assez vite pour que la réponse paraisse immédiate, et assez juste pour que le modèle de langage comprenne l'intention. Les erreurs qui coûtent cher sont celles sur les noms de pièces et d'appareils, et sur les nombres (« mets le chauffage à 21 »).

## Situation actuelle

[jabfy-voice](../composants/README.md) utilise **faster-whisper** avec le modèle `base`, sur CPU, quantifié en `int8`, langue forcée en français.

## Les solutions existantes

- **Whisper (OpenAI)** — modèle de référence, multilingue (99 langues), en plusieurs tailles : `tiny` (39 M de paramètres), `base` (74 M), `small` (244 M), `medium` (769 M), `large-v3` (1,55 G) et `turbo` (809 M, presque aussi précis que `large-v3` mais bien plus rapide).
- **faster-whisper** — réimplémentation de Whisper sur CTranslate2 : mêmes modèles et même précision, jusqu'à 4 fois plus rapide, et moins de mémoire grâce à la quantification `int8`.
- **whisper.cpp** — Whisper en C/C++, optimisé pour le CPU et l'embarqué.
- **Vosk** — moteur basé sur Kaldi, très léger, avec reconnaissance en flux (le texte arrive pendant que l'on parle).
- **Parakeet TDT 0.6B v3 (NVIDIA)** — modèle récent pour 25 langues européennes dont le français, très rapide sur GPU NVIDIA.
- **Voxtral (Mistral AI)** — modèles de transcription récents, à l'aise en français, mais plus lourds (3 milliards de paramètres pour le plus petit).

## Comparatif

| Solution | 100 % local | Latence | Qualité en français | Mémoire | Licence |
|---|---|---|---|---|---|
| faster-whisper `base` (actuel) | Oui | Faible sur CPU | Correcte, nettement en dessous de `small` | ~1 Go | MIT (code et poids) |
| faster-whisper `small` | Oui | Moyenne sur CPU | Bonne | ~2 Go | MIT |
| faster-whisper `turbo` | Oui | Élevée sur CPU, faible sur GPU | Très bonne | ~6 Go | MIT |
| whisper.cpp | Oui | Faible à moyenne sur CPU selon la taille | Identique à Whisper (mêmes poids) | Selon la taille, réduite par quantification | MIT |
| Vosk, grand modèle français | Oui | Faible, en flux | WER 14,7 % sur Common Voice | 1,4 Go | Apache 2.0 |
| Vosk, petit modèle français | Oui | Très faible, en flux | WER 24 % sur Common Voice | 41 Mo | Apache 2.0 |
| Parakeet TDT 0.6B v3 | Oui | Très faible sur GPU NVIDIA | Bonne (25 langues européennes) | GPU recommandé | CC-BY-4.0 |
| Voxtral Mini | Oui | Élevée sans GPU | Très bonne en français | GPU recommandé (3 G de paramètres) | Apache 2.0 |

Mémoire : ordres de grandeur publiés par OpenAI pour Whisper, et par Alpha Cephei pour Vosk. Les WER Vosk sont ceux publiés par Alpha Cephei ; ceux de Jabfy, sur nos propres phrases de commande, restent à mesurer : voir [Performance › WER](../performance/stt-wer.md).

## Choix retenu

**faster-whisper**, déjà en place dans jabfy-voice, est confirmé :

- même qualité que Whisper, plus rapide et plus léger, et licence MIT pour le code comme pour les poids ;
- fonctionne sans GPU, ce qui correspond à la cible « box domestique ».

Une décision reste à prendre sur **la taille du modèle** : `base` est rapide mais fait plus d'erreurs ; `small` est probablement le bon compromis sur CPU. Elle sera tranchée par la mesure du WER sur notre jeu de phrases.

Solutions écartées pour l'instant :

- **Vosk** : plus léger et en flux, mais sensiblement moins précis. À garder en réserve pour un satellite très peu puissant.
- **Parakeet et Voxtral** : très bons, mais pensés pour un GPU, que la cible n'aura pas forcément. À suivre.
- **Whisper d'origine (openai-whisper)** : même précision que faster-whisper, mais plus lent.

## Avancées récentes

- **Whisper `large-v3-turbo`** (fin 2024) : qualité proche de `large-v3` pour une fraction du temps de calcul.
- **Parakeet TDT 0.6B v3** (2025) : NVIDIA étend à 25 langues européennes, dont le français, un modèle auparavant anglais.
- **Voxtral** (2025) : Mistral AI publie sous licence Apache 2.0 des modèles de transcription à l'aise en français.

## Sources

- [OpenAI Whisper — tailles et mémoire des modèles](https://github.com/openai/whisper)
- [faster-whisper (SYSTRAN)](https://github.com/SYSTRAN/faster-whisper)
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp)
- [Vosk — catalogue des modèles et WER](https://alphacephei.com/vosk/models)
- [NVIDIA Parakeet TDT 0.6B v3 — fiche du modèle](https://catalog.ngc.nvidia.com/orgs/nvidia/-/collections/parakeet-tdt-0.6b/)
- [Voxtral vs Whisper 2026 (comparatif tiers)](https://weesperneonflow.ai/en/blog/2026-03-31-voxtral-whisper-open-source-speech-models-comparison-2026/)
- [Best open source speech-to-text models in 2026 (comparatif tiers)](https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks)
