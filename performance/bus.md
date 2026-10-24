# Débit et latence du bus

| Responsable | Valeur de départ | Cible | Dernière mesure |
|---|---|---|---|
| | | | |

## Définition

- **Débit** : nombre de messages normalisés par seconde que le bus absorbe sans perte ni retard croissant.
- **Latence** : temps entre la réception d'un message par un adapter et sa livraison aux abonnés, puis entre `command.requested` et `command.executed`.

## Protocole de mesure

- Injection de télémétrie à débit croissant par jabfy-simulation, jusqu'à saturation.
- Horodatages lus dans les messages (`timestamp`) et dans l'audit.
- Médiane et p95 à chaque palier de débit.

## Résultats

| Date | Commit jabfy-bus | Adapter | Débit injecté | Débit absorbé | Latence médiane | p95 |
|---|---|---|---|---|---|---|
| | | | | | | |

## Optimisations testées

| Date | Optimisation | Avant | Après | Gardée ? |
|---|---|---|---|---|
| | | | | |
