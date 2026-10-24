# ADR-0001 — Consigner les décisions dans des ADR

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté | 2026-10-24 | Elias | |

## Contexte

Le projet est réparti sur une douzaine de repos et cinq personnes. Les choix techniques se font en RDV ou dans des PR, puis se perdent : on ne sait plus pourquoi une techno a été retenue, ni ce qui avait été écarté. L'objectif obligatoire 2 de l'EIP demande une architecture documentée.

## Options étudiées

1. **Ne rien formaliser** — aucun coût, mais les raisons des choix disparaissent avec les conversations.
2. **Un document d'architecture unique** — tout au même endroit, mais il devient vite long et on ne voit plus ce qui a changé ni quand.
3. **Une fiche courte par décision (ADR)** — chaque décision est datée, relue en PR et jamais réécrite.

## Décision

Option 3 : chaque décision structurante fait l'objet d'un ADR dans `architecture/adr/` de jabfy-docs, selon le [modèle](modele.md).

## Conséquences

- Les choix déjà faits (FastAPI, modèle local, Electron/React) sont consignés rétroactivement, à commencer par les ADR 0002 à 0004.
- Une décision prise en RDV n'est définitive qu'une fois son ADR fusionné.
- Il faut tenir l'[index](README.md) à jour.
