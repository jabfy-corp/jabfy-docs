# Architecture

> Objectif obligatoire 2 : *Structure, document and make your technical architecture reliable.*

L'architecture est décrite à quatre niveaux, du plus général au plus précis :

| Page | Question à laquelle elle répond |
|---|---|
| [Vue globale (C4)](vue-globale.md) | Quels sont les blocs, et qui parle à qui ? |
| [Flux d'une demande](flux.md) | Que se passe-t-il entre « Jabfy, allume le salon » et la réponse vocale ? |
| [Interfaces](interfaces.md) | Quels contrats lient les repos entre eux ? |
| [CI/CD](ci-cd.md) | Comment chaque repo est testé, construit et livré ? |
| [ADR](adr/README.md) | Pourquoi ces choix, et pas d'autres ? |

## Règles

- Les diagrammes sont écrits en **Mermaid** dans les pages, donc versionnés avec le texte. Dans GitBook, l'intégration Mermaid doit être activée pour les afficher.
- Une décision structurante (techno, protocole, découpage) donne lieu à un **ADR**, qui renvoie vers la fiche de [veille](../veille/README.md) d'où elle vient.
- Le détail interne d'un composant reste dans le `docs/` de son repo et apparaît dans [Composants](../composants/README.md). Ici, on ne décrit que ce qui traverse plusieurs repos.
