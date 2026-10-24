# LLM local

| Statut | Responsable | Dernière mise à jour |
|---|---|---|
| À faire | | |

## Le problème

Transformer une demande en langage naturel en une proposition d'action JSON valide, sur une machine domestique sans GPU dédié, en quelques secondes au plus. Le modèle ne doit jamais exécuter lui-même : il propose, la vérification décide.

## Situation actuelle

- [jabfy-core](https://github.com/jabfy-corp/jabfy-core) parle à n'importe quel serveur exposant une API compatible OpenAI (llama.cpp, Ollama) et expose les paramètres d'échantillonnage.
- [jabfy-deploy](https://github.com/jabfy-corp/jabfy-deploy) lance Ollama et télécharge `qwen2.5:1.5b` par défaut.
- [jabfy-voice](https://github.com/jabfy-corp/jabfy-voice) utilise `llama3.2` via Ollama.

Voir aussi [ADR-0003](../architecture/adr/0003-modele-local.md).

## Les solutions existantes

Deux choix distincts à documenter :

- **Serveur d'inférence** : Ollama, llama.cpp (`llama-server`)…
- **Modèle** : qwen2.5, llama3.2…

## Comparatif

| Modèle | Taille / quantification | 100 % local | Latence | Qualité en français | Taux de JSON valide | RAM | Licence |
|---|---|---|---|---|---|---|---|
| qwen2.5:1.5b | | | | | | | |
| llama3.2 | | | | | | | |

Protocole de mesure : [Performance › Compréhension des intentions](../performance/intentions.md).

## Choix retenu

## Avancées récentes

## Sources
