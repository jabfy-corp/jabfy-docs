# Performance

> Objectif complémentaire D : *Measure, test and optimize technical performance.*

Chaque métrique a sa page, construite sur le même [modèle](modele.md) : définition, protocole de mesure, valeur de départ, cible, résultats, optimisations testées.

## Métriques suivies

| Métrique | Page | Départ | Cible | Dernière mesure |
|---|---|---|---|---|
| Latence de bout en bout et par étape | [Latence](latence.md) | | | |
| Taux d'erreur du STT (WER) en français | [WER](stt-wer.md) | | | |
| Faux déclenchements du wake word par heure | [Wake word](wake-word.md) | | | |
| Taux de compréhension des intentions | [Intentions](intentions.md) | | | |
| CPU et RAM sur la machine cible | [Ressources](ressources.md) | | | |
| Débit et latence du bus | [Bus](bus.md) | | | |

## Règles de mesure

- **Reproductible** : chaque mesure indique le commit de chaque repo, la machine, le modèle et sa version. Les scénarios passent par [jabfy-simulation](https://github.com/jabfy-corp/jabfy-simulation), pour pouvoir les rejouer à l'identique et les lancer en CI.
- **Machine cible** : à définir une fois pour toutes (CPU, RAM, GPU ou non, OS), puis décrite ci-dessous.
- **Une seule variable à la fois** : une optimisation ne compte que si elle est mesurée avant et après, toutes choses égales par ailleurs.
- **Médiane et p95** plutôt que moyenne pour les latences.

## Machine cible

| Élément | Valeur |
|---|---|
| CPU | |
| RAM | |
| GPU | |
| OS | |
