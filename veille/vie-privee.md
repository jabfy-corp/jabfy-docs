# Vie privée

| Statut | Responsable | Dernière mise à jour |
|---|---|---|
| À faire | | |

## Le problème

Garantir, et pouvoir démontrer, qu'aucune donnée personnelle (voix, transcriptions, habitudes, état de la maison) ne quitte le réseau local, alors que l'assistant écoute, raisonne et garde un journal d'audit.

## Questions à traiter

- Quelles dépendances font des appels réseau sortants (téléchargement de modèles, télémétrie) et comment les couper ?
- Comment prouver l'absence de trafic sortant (capture réseau pendant un scénario de [jabfy-simulation](https://github.com/jabfy-corp/jabfy-simulation)) ?
- Que contient le journal d'audit, combien de temps le garder, comment le chiffrer ?
- Comment l'utilisateur consulte et efface ses données ?

## Les solutions existantes

À compléter : approches des assistants comparables (Home Assistant Assist, assistants cloud), techniques de minimisation et de chiffrement au repos.

## Comparatif

| Solution | 100 % local | Latence | Qualité en français | RAM | Licence | Données conservées |
|---|---|---|---|---|---|---|
| | | | | | | |

## Choix retenu

Lien avec la conformité : [Protection › RGPD](../protection/rgpd.md).

## Avancées récentes

## Sources
