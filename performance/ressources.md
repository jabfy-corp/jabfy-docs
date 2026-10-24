# CPU et RAM

| Responsable | Valeur de départ | Cible | Dernière mesure |
|---|---|---|---|
| | | | |

## Définition

Consommation CPU (moyenne et pic) et mémoire résidente de chaque conteneur ou processus, au repos et pendant un scénario, sur la [machine cible](README.md).

## Protocole de mesure

- Stack lancée par jabfy-deploy.
- Relevé avec `docker stats` pendant un scénario jabfy-simulation, puis au repos.
- Le serveur de modèles est mesuré à part, modèle chargé.

## Résultats

| Date | Composant | Au repos : CPU / RAM | En scénario : CPU / RAM | Commentaire |
|---|---|---|---|---|
| | jabfy-sim | | | |
| | core | | | |
| | ollama | | | |
| | mosquitto | | | |

## Optimisations testées

| Date | Optimisation | Avant | Après | Gardée ? |
|---|---|---|---|---|
| | | | | |
