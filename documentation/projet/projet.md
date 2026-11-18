# Vision

Jabfy n'est pas un chatbot de plus : c'est une **couche d'orchestration locale** qui relie des données brutes, un raisonnement par IA et des actions réelles, en passant toujours par une vérification.

On veut passer de « je demande, il répond » à « il comprend, puis il agit ».

## Principes

* **Vie privée d'abord** : tout tourne sur place, aucune donnée ne quitte la maison.
* **Sécurité dès la conception** : chaque action est vérifiée avant d'être exécutée.
* **Modularité** : chaque composant est indépendant et remplaçable.
* **Extensibilité** : un nouveau protocole ou un nouvel appareil passe par un format standard, le bus JSON.
* **Transparence** : chaque décision est traçable dans un journal d'audit.

## Périmètre de l'EIP

L'EIP se concentre sur un cœur fiable et sûr :

* maison connectée et IoT uniquement ;
* normalisation fiable des données (bus JSON universel) ;
* moteur de vérification solide, pensé sécurité d'abord ;
* décisions locales à faible latence ;
* maison simulée pour démontrer des scénarios réels.

Sont exclus pour l'instant : e-mails, calendriers, messageries et intégrations d'entreprise.

## Objectifs EIP retenus

| Objectif         | Intitulé                                                               | Section                                         | Où en est-on (27/10/2026)                                                                                                                |
| ---------------- | ---------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Obligatoire 1    | Track what's out there and use it to crack your project's hard problem | [Veille](../veille/veille/)                     | Une fiche par projet qui contient du code (9) et 6 études par domaine ; choix confirmés pour STT, TTS et protocoles, mesurés pour le LLM |
| Obligatoire 2    | Structure, document and make your technical architecture reliable      | [Architecture](../architecture/architecture.md) | Modèle C4, flux, contrats, CI/CD, 10 ADR ; convergence de la V0.0.1 sur `main` en cours                                                  |
| Complémentaire A | Protect and make the most of your technology                           | [Protection](../protection/protection.md)       | État des lieux fait (licences, sécurité, RGPD) ; démarches EPITECH et INPI à lancer                                                      |
| Complémentaire D | Measure, test and optimize technical performance                       | [Performance](../performance/performance/)      | Premières mesures réelles (bus, modèle) et scripts reproductibles ; STT et wake word à mesurer                                           |

## Après l'EIP

Intégrations multi-domaines (e-mail, calendrier, communication), écosystèmes multi-appareils (maison, voiture, bureau), réseaux locaux distribués, matériel dédié basse consommation.
