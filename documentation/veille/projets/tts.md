# jabfy-tts : répondre à voix haute

| Responsable | Code | Mise à jour |
|---|---|---|
| Eloi | Rust ; `main` | 18/11/2026 |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par le responsable.

## Le problème constaté

- **Une voix française naturelle, sans GPU et sans cloud.** La voix système actuelle de jabfy-voice (eSpeak NG) est robotique.
- **Commencer à parler avant que le modèle ait fini d'écrire** sa réponse, sinon l'attente s'additionne.

## Les technologies et pourquoi

| Besoin | Choix | Pourquoi | Écarté |
|---|---|---|---|
| Modèle de voix | Kokoro-82M ([ADR-0009](../../architecture/adr/0009-kokoro-tts.md)) | Meilleur compromis qualité et taille sur CPU ; poids sous licence Apache 2.0 | Piper : passé en GPL-3.0. XTTS-v2 : licence non commerciale. Chatterbox : trop lourd sans GPU |
| Exécution | Rust, avec `kokoroxide` et ONNX Runtime (`ort`) | Un binaire sans interpréteur, faible empreinte mémoire | JavaScript (kokoro-js) : première version, remplacée par Rust le 12/10/2026 |
| Parler tôt | Mode flux : chaque phrase est synthétisée dès qu'elle est complète | Le premier son arrive après la première phrase, pas après toute la réponse | — |
| Texte vers phonèmes | eSpeak NG | Imposé par Kokoro | — |

## Ce que la veille change

- **Dépendance fragile.** La version publiée de `kokoroxide` dépend d'une version d'ONNX Runtime retirée de crates.io : le projet ne compile qu'avec une branche non fusionnée d'un fork. Si ce fork disparaît, jabfy-tts ne compile plus. Alternatives à évaluer : `kokoro-onnx` ou le paquet officiel `kokoro`, tous deux en Python, le langage du reste de la pile.
- **Relier la voix (Python) et la synthèse (Rust)** : bibliothèque Python de Kokoro, ou service jabfy-tts appelé par Core. Décision à prendre, liée à la direction « orchestrateur ».
- **Une seule voix française**, de qualité moyenne, à créditer (données SIWIS sous CC BY).

## Sources

- [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M), [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx), [ort](https://github.com/pykeio/ort)
- [kokoroxide, PR de migration vers ort 2](https://github.com/dhruv304c2/kokoroxide/pull/2)
- Étude détaillée : [TTS](../tts.md)
