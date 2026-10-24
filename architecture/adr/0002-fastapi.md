# ADR-0002 — FastAPI pour les API Python

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Proposé (rétroactif) | | | |

> Décision déjà appliquée, consignée après coup. Contexte et options à compléter par l'équipe avant de passer en « Accepté ».

## Contexte

jabfy-core expose une API HTTP consommée par les clients desktop, web et mobile, et par la simulation. Le reste de la chaîne (bus, guard, simulation, voix) est écrit en Python, et les contrats de données doivent rester stricts et documentés. FastAPI était déjà utilisé dans jabfy-prototype.

## Options étudiées

1. **FastAPI** — validation des entrées par Pydantic (déjà utilisé par jabfy-guard), OpenAPI générée automatiquement, support natif de l'asynchrone et des WebSockets.
2. **Flask** — à compléter.
3. **Serveur Node.js (Express)** — à compléter.

## Décision

Les API HTTP écrites en Python utilisent FastAPI.

## Conséquences

- Le contrat de l'API de Core est l'OpenAPI générée : elle peut être exportée et publiée dans la doc (voir [Interfaces](../interfaces.md)).
- Les schémas Pydantic deviennent la source de vérité des formats d'entrée et de sortie.
- À compléter.
