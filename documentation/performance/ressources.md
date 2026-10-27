# CPU et RAM

| Suivi par | Valeur de départ | Cible | Dernière mesure |
|---|---|---|---|
| Loan | Modèles : 2,0 Go (Llama 3.2 3B) à 6,0 Go (Ministral 3 8B) | À fixer avec la machine cible | 27/10/2026 (tailles des modèles) |

## Définition

Consommation CPU (moyenne et pic) et mémoire résidente de chaque conteneur ou processus, au repos et pendant un scénario, sur la [machine cible](README.md).

## Protocole de mesure

- Stack lancée par jabfy-deploy.
- Relevé avec `docker stats` pendant un scénario jabfy-simulation, puis au repos.
- Le serveur de modèles est mesuré à part, modèle chargé.

## Résultats

| Date | Composant | Au repos : CPU / RAM | En scénario : CPU / RAM | Commentaire |
|---|---|---|---|---|
| 27/10/2026 | Modèle Llama 3.2 3B (Q4_K_M) | 2,0 Go sur disque | Chargé en mémoire GPU ou RAM | Mesuré avec `ollama list` |
| 27/10/2026 | Modèle Ministral 3 8B (Q4_K_M) | 6,0 Go sur disque | Chargé en mémoire GPU ou RAM | Mesuré avec `ollama list` |
| | jabfy-sim | | | |
| | core | | | |
| | ollama | | | |
| | mosquitto | | | |

## Optimisations testées

| Date | Optimisation | Avant | Après | Gardée ? |
|---|---|---|---|---|
| | | | | |
