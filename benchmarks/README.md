# Benchmarks

Scripts de mesure utilisés par les pages Performance du site. Ils sont ici, hors du dossier `documentation/`, pour que n'importe qui puisse relancer une mesure et comparer.

| Script | Mesure | Page du site |
|---|---|---|
| `bench_bus.py` | Débit de télémétrie, latence d'une commande (vérification, exécution, audit), mémoire retenue | Performance › Débit et latence du bus |
| `bench_llm.py` | Latence du modèle, JSON valide, bonne action sur 10 consignes en français | Performance › Compréhension des intentions |

## Lancer

Depuis la racine de `jabfy-docs`, avec les repos Jabfy clonés côte à côte :

```bash
# Bus : bibliothèque standard uniquement
PYTHONPATH=../jabfy-bus python3 benchmarks/bench_bus.py

# Modèle : Ollama démarré, modèles téléchargés
ollama pull llama3.2 && ollama pull ministral-3
python3 benchmarks/bench_llm.py
```

`bench_llm.py` reprend le prompt système, le format de message, le parseur et la règle de vérification de jabfy-core, pour mesurer ce que Core recevrait réellement.

## Résultats

Un fichier par campagne dans `resultats/`, nommé par date, avec en tête la version du code et la machine.

Règles : noter le commit de chaque repo mesuré, ne changer qu'une variable à la fois, et toujours préciser la machine. Une mesure sur une machine de développement avec GPU ne dit rien de la box cible.
