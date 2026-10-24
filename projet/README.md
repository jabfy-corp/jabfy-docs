# Vision

Jabfy n'est pas un chatbot de plus : c'est une **couche d'orchestration locale** qui relie des données brutes, un raisonnement par IA et des actions réelles, en passant toujours par une vérification.

On veut passer de « je demande, il répond » à « il comprend, puis il agit ».

## Principes

- **Vie privée d'abord** : tout tourne sur place, aucune donnée ne quitte la maison.
- **Sécurité dès la conception** : chaque action est vérifiée avant d'être exécutée.
- **Modularité** : chaque composant est indépendant et remplaçable.
- **Extensibilité** : un nouveau protocole ou un nouvel appareil passe par un format standard, le bus JSON.
- **Transparence** : chaque décision est traçable dans un journal d'audit.

## Périmètre de l'EIP

L'EIP se concentre sur un cœur fiable et sûr :

- maison connectée et IoT uniquement ;
- normalisation fiable des données (bus JSON universel) ;
- moteur de vérification solide, pensé sécurité d'abord ;
- décisions locales à faible latence ;
- maison simulée pour démontrer des scénarios réels.

Sont exclus pour l'instant : e-mails, calendriers, messageries et intégrations d'entreprise.

## Objectifs EIP retenus

| Objectif | Intitulé | Section |
|---|---|---|
| Obligatoire 1 | Track what's out there and use it to crack your project's hard problem | [Veille](../veille/README.md) |
| Obligatoire 2 | Structure, document and make your technical architecture reliable | [Architecture](../architecture/README.md) |
| Complémentaire A | Protect and make the most of your technology | [Protection](../protection/README.md) |
| Complémentaire D | Measure, test and optimize technical performance | [Performance](../performance/README.md) |

## Après l'EIP

Intégrations multi-domaines (e-mail, calendrier, communication), écosystèmes multi-appareils (maison, voiture, bureau), réseaux locaux distribués, matériel dédié basse consommation.
