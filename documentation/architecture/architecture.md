# En bref

> Objectif obligatoire 2 : _Structure, document and make your technical architecture reliable._

## En bref

* **Une règle structure tout : l'IA propose, Guard autorise, le Bus exécute.** Le modèle de langage ne pilote jamais un appareil directement ([ADR-0007](adr/0007-ia-propose-guard-decide.md)).
* **Un contrat commun** : tous les composants échangent des messages JSON versionnés, décrits par un schéma ([Interfaces](interfaces.md)).
* **Tout est local** : transcription, modèle de langage, synthèse et décisions tournent sur la machine de la maison.
* **Tout est tracé** : chaque décision est écrite dans un journal d'audit infalsifiable, avant l'exécution.
* **La V0.0.1 tourne** : maison virtuelle 3D pilotée par l'IA, lancée en une commande. Sa convergence sur `main` est le prochain chantier.

## Pages

| Page                               | Question à laquelle elle répond                                                |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| [Vue globale (C4)](vue-globale.md) | Quels sont les blocs, qui parle à qui, et qu'est-ce qui tourne aujourd'hui ?   |
| [Flux d'une demande](flux.md)      | Que se passe-t-il entre la demande et l'action, aujourd'hui et dans la cible ? |
| [Interfaces](interfaces.md)        | Quels contrats lient les repos entre eux ?                                     |
| [CI/CD](ci-cd.md)                  | Comment chaque repo est testé, construit et livré ?                            |
| [ADR](adr/)                        | Pourquoi ces choix, et quelles décisions restent à prendre ?                   |

## Fiabilité : ce qui est en place

| Mécanisme                                               | Où                          | Effet                                                    |
| ------------------------------------------------------- | --------------------------- | -------------------------------------------------------- |
| Refus par défaut                                        | jabfy-bus, jabfy-guard      | Une commande à risque sans règle explicite est refusée   |
| Admission à usage unique                                | jabfy-bus                   | Une approbation ne peut être rejouée ni modifiée         |
| Audit chaîné en SHA-256, écrit avant envoi              | jabfy-bus                   | Toute falsification se détecte ; pas d'action sans trace |
| Validation des messages contre le schéma                | jabfy-bus                   | Un message mal formé est rejeté à l'entrée               |
| API de consultation en lecture seule, origines filtrées | jabfy-bus                   | Aucune commande ne passe par le web                      |
| Tests automatisés en CI                                 | bus (96), core (30), deploy | Régressions détectées avant fusion                       |
| Lancement en une commande, avec contrôles de santé      | jabfy-deploy                | Pile reproductible sur toute machine avec Docker         |

Les points faibles connus sont listés dans [CI/CD](ci-cd.md) et dans la page [Performance](../performance/performance/).

## Règles de documentation

* Les diagrammes sont écrits en **Mermaid** dans les pages, donc versionnés avec le texte.
* Une décision structurante donne lieu à un **ADR**, qui renvoie vers la fiche de [veille](../veille/veille/) d'où elle vient.
* Le détail interne d'un composant reste dans le `docs/` de son repo et apparaît dans [Composants](../composants/composants.md). Ici, on ne décrit que ce qui traverse plusieurs repos.
