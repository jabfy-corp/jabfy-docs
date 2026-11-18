# Synthèse vocale (TTS)

| Statut                                                   | Suivi par | Dernière mise à jour |
| -------------------------------------------------------- | --------- | -------------------- |
| Première version : choix confirmé, intégration à décider | Eloi      | 27/10/2026           |

## Le problème

Lire la réponse à voix haute en français, sur la machine, avec une voix naturelle, et commencer à parler avant que le modèle ait fini d'écrire sa réponse (lecture phrase par phrase). La synthèse doit tenir sur une machine sans GPU.

## Situation actuelle

Deux solutions coexistent :

* [jabfy-tts](../../composants/composants.md) est une bibliothèque Rust autour de **Kokoro-82M** (via kokoroxide), avec un mode « flux » qui synthétise chaque phrase dès qu'elle est complète.
* [jabfy-voice](../../composants/composants.md) utilise **pyttsx3**, qui pilote le moteur vocal du système : eSpeak NG sous Linux.

## Les solutions existantes

* **Kokoro-82M** — petit modèle (82 millions de paramètres) à la qualité remarquable pour sa taille ; une voix française (`ff_siwis`).
* **Piper** — synthèse très rapide sur CPU, pensée pour le Raspberry Pi, avec de nombreuses voix françaises. Son développement a migré vers un nouveau dépôt, sous licence GPL-3.0.
* **eSpeak NG** — synthèse par règles, minuscule, mais voix très robotique. C'est ce qu'utilise pyttsx3 sous Linux.
* **Chatterbox (Resemble AI)** — modèle récent, très naturel, multilingue, avec clonage de voix ; plus lourd.
* **XTTS-v2 (Coqui)** — très bonne qualité et clonage de voix, mais licence non commerciale, et la société Coqui a fermé.

## Comparatif

| Solution               | 100 % local | Latence au premier son            | Qualité en français                                          | Ressources                 | Licence (code / voix)                                       |
| ---------------------- | ----------- | --------------------------------- | ------------------------------------------------------------ | -------------------------- | ----------------------------------------------------------- |
| Kokoro-82M (jabfy-tts) | Oui         | Faible sur CPU, phrase par phrase | Bonne ; une seule voix française, notée B- par la communauté | Faible, CPU                | Apache 2.0 / voix française issue de données SIWIS en CC BY |
| Piper                  | Oui         | Très faible sur CPU               | Correcte à bonne selon la voix                               | Très faible (Raspberry Pi) | GPL-3.0 depuis la migration / licence propre à chaque voix  |
| eSpeak NG (pyttsx3)    | Oui         | Immédiate                         | Robotique                                                    | Minime                     | GPL-3.0                                                     |
| Chatterbox             | Oui         | Moyenne, GPU conseillé            | Très naturelle (multilingue)                                 | Élevée                     | MIT                                                         |
| XTTS-v2                | Oui         | Moyenne, GPU conseillé            | Très naturelle                                               | Élevée                     | **Non commerciale (Coqui Public Model License)**            |

La latence au premier son de Jabfy fait partie de la [latence de bout en bout](../../performance/latence.md) (étape `t_tts`).

## Choix retenu

**Kokoro-82M, via jabfy-tts**, est confirmé comme moteur de synthèse :

* meilleur compromis qualité / taille de la liste, sur CPU ;
* licence Apache 2.0 pour les poids, sans restriction commerciale ;
* le mode flux de jabfy-tts répond au besoin de parler avant la fin de la réponse.

Points de vigilance :

* **une seule voix française**, de qualité moyenne, et soumise à attribution (données SIWIS en CC BY) : à créditer dans le produit ;
* **pyttsx3 est à retirer de jabfy-voice** au profit de Kokoro. Comme jabfy-tts est en Rust et jabfy-voice en Python, il faut décider comment les relier (bibliothèque Python de Kokoro ou service jabfy-tts appelé par la voix) : décision à prendre en équipe et à consigner dans un ADR.

Solutions écartées :

* **Piper** : excellent sur petit matériel, mais le passage du moteur en GPL-3.0 impose ses obligations à tout logiciel qui l'intègre. À garder en réserve pour un satellite très peu puissant.
* **Chatterbox** : qualité supérieure, mais trop lourd pour une box sans GPU.
* **XTTS-v2** : licence non commerciale, et projet sans éditeur depuis la fermeture de Coqui.
* **eSpeak NG** : trop robotique pour un assistant grand public.

## Avancées récentes

* **Kokoro v1.0** (début 2025) a ajouté le multilingue, dont le français.
* **Piper** a été archivé en octobre 2025 ; le développement continue sous GPL-3.0 dans le dépôt de l'Open Home Foundation.
* **Chatterbox Multilingual** (Resemble AI) publie sous licence MIT un modèle multilingue très naturel.
* Les modèles très compacts se multiplient (autour de 100 M de paramètres), ce qui rend la synthèse naturelle réaliste sur CPU.

## Sources

* [Kokoro-82M — fiche du modèle (Hugging Face)](https://huggingface.co/hexgrad/Kokoro-82M)
* [Kokoro — voix et notes de qualité (miroir communautaire)](https://huggingface.co/simonfxr/kokoro.cpp-GGUF)
* [Piper — nouveau dépôt OHF-Voice/piper1-gpl](https://github.com/OHF-Voice/piper1-gpl)
* [Revue de Piper et de son changement de licence (article tiers)](https://www.promptquorum.com/power-local-llm/piper-tts-review)
* [Comparatif des TTS open source par licence (Cartesia)](https://www.cartesia.ai/learn/open-source-tts)
* [Kokoro vs XTTS vs Chatterbox (comparatif tiers)](https://localaimaster.com/blog/kokoro-vs-xtts-vs-chatterbox)
