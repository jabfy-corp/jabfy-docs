# Latence de bout en bout

| Suivi par | Valeur de départ           | Cible                                                        | Dernière mesure         |
| --------- | -------------------------- | ------------------------------------------------------------ | ----------------------- |
| Loan      | Partie texte : 0,3 à 3,6 s | < 3 s du silence à la première syllabe, sur la machine cible | 27/10/2026 (par étapes) |

## Définition

Temps entre la fin de la phrase de l'utilisateur et le premier son de la réponse, décomposé par étape (voir [Flux d'une demande](../architecture/flux.md)) :

`t_total = t_stt + t_llm + t_verif + t_exec + t_tts`

`t_wake` (détection du mot d'activation) est mesuré à part, car il précède la fin de la phrase.

Tant que la voix n'est pas branchée sur Core, on mesure la partie texte : de la demande reçue par Core jusqu'au nouvel état de l'appareil (`t_llm + t_verif + t_exec`).

## Protocole de mesure

* **Par étape**, dès maintenant : chaque composant est mesuré seul avec les scripts de [`benchmarks/`](../../benchmarks/).
* **De bout en bout**, une fois la voix branchée : scénarios jabfy-simulation (commande simple, commande refusée, demande hors sujet), horodatage de chaque étape grâce au `correlation_id` qui suit la demande, 30 exécutions par scénario, médiane et p95.

## Résultats par étape

Machine : i7-13700HX, RTX 5060 Laptop 8 Go (voir [Machines](performance/)).

| Date       | Étape              | Composant         | Configuration                           | Médiane | Source                      |
| ---------- | ------------------ | ----------------- | --------------------------------------- | ------- | --------------------------- |
| 27/10/2026 | `t_llm`            | Modèle via Ollama | Llama 3.2 3B, GPU                       | 0,33 s  | [Intentions](intentions.md) |
| 27/10/2026 | `t_llm`            | Modèle via Ollama | Llama 3.2 3B, CPU seul                  | 1,13 s  | [Intentions](intentions.md) |
| 27/10/2026 | `t_llm`            | Modèle via Ollama | Ministral 3 8B, GPU                     | 1,08 s  | [Intentions](intentions.md) |
| 27/10/2026 | `t_llm`            | Modèle via Ollama | Ministral 3 8B, CPU seul                | 3,55 s  | [Intentions](intentions.md) |
| 27/10/2026 | `t_verif + t_exec` | jabfy-bus         | Audit sur disque avec `fsync`           | 0,65 ms | [Bus](bus.md)               |
| À mesurer  | `t_stt`            | jabfy-voice       | faster-whisper `base` puis `small`, CPU | —       | [WER](stt-wer.md)           |
| À mesurer  | `t_tts`            | jabfy-tts         | Kokoro-82M, premier son, CPU            | —       | —                           |

## Lecture

Sur la partie déjà mesurée, **plus de 99 % du temps est passé dans le modèle de langage**. Les optimisations utiles porteront donc sur le choix et la configuration du modèle (taille, quantification, longueur de la réponse), pas sur le bus. La synthèse phrase par phrase de jabfy-tts devrait permettre de commencer à parler avant la fin de la génération.

## Optimisations à tester

| Date    | Optimisation                                                             | Avant | Après | Gardée ? |
| ------- | ------------------------------------------------------------------------ | ----- | ----- | -------- |
| À faire | Réponse plus courte (limiter `max_tokens`, `action_chain` en une phrase) | —     | —     | —        |
| À faire | Garder le modèle chargé en mémoire entre deux demandes                   | —     | —     | —        |
| À faire | Lecture de la réponse phrase par phrase (flux jabfy-tts)                 | —     | —     | —        |
