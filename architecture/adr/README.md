# Décisions d'architecture (ADR)

Un ADR (*Architecture Decision Record*) est une fiche courte qui consigne **une** décision : le contexte, les options étudiées, ce qui a été décidé et ce que ça implique. C'est le lien entre la [veille](../../veille/README.md) et l'architecture.

## Quand en écrire un

- Choix d'une techno, d'un modèle, d'un protocole ou d'un format.
- Découpage ou fusion de composants.
- Changement incompatible d'un [contrat d'interface](../interfaces.md).

## Comment

1. Copier le [modèle](modele.md) sous `NNNN-titre-court.md`, avec le numéro suivant.
2. L'ajouter dans `SUMMARY.md` et dans le tableau ci-dessous.
3. Ouvrir une PR : la discussion de la PR sert de revue de la décision.

Un ADR accepté ne se réécrit pas. Si la décision change, on écrit un nouvel ADR et on passe l'ancien en « Remplacé par ADR-NNNN ».

## Statuts

`Proposé` → `Accepté` → éventuellement `Remplacé par ADR-NNNN` ou `Abandonné`.

## Index

| # | Décision | Statut | Date |
|---|---|---|---|
| [0001](0001-consigner-les-decisions.md) | Consigner les décisions dans des ADR | Accepté | 2026-10-24 |
| [0002](0002-fastapi.md) | FastAPI pour les API Python | Proposé (rétroactif) | |
| [0003](0003-modele-local.md) | Modèle local via une API compatible OpenAI | Proposé (rétroactif) | |
| [0004](0004-electron-react.md) | Electron et React pour le client desktop | Proposé (rétroactif) | |
