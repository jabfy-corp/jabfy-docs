# ADR-0002 — FastAPI pour les API Python

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté (consigné a posteriori) | 27/10/2026 | Équipe | — |

## Contexte

Plusieurs composants Python exposent une API HTTP : jabfy-core (propositions d'actions), jabfy-simulation (interface 3D et inventaire de la maison) et, en option, jabfy-bus (consultation). Ces API échangent des structures strictes (états d'appareils, propositions, paramètres de génération) qui doivent être validées à l'entrée, et documentées pour les autres repos. Le premier prototype utilisait déjà FastAPI.

## Options étudiées

1. **FastAPI** — validation des entrées par Pydantic, spécification OpenAPI et page Swagger générées automatiquement, asynchrone et WebSocket natifs.
2. **Flask** — très simple et répandu, mais validation et documentation à ajouter à la main (extensions).
3. **Node.js (Express)** — l'écosystème des clients web, mais une seconde pile de langage côté serveur, alors que l'IA, la voix et le bus sont en Python.

## Décision

Les API HTTP écrites en Python utilisent **FastAPI**, avec des schémas Pydantic comme contrat d'entrée et de sortie.

## Conséquences

- Le contrat de chaque API est son **OpenAPI générée** : jabfy-core le sert sur `/docs` et `/openapi.json`, et il peut être publié dans la doc ([Interfaces](../interfaces.md)).
- Une requête invalide est rejetée avant d'atteindre la logique (code 422), y compris un champ inconnu.
- Exception tolérée : l'interface web de jabfy-voice, en Flask, très simple et en lecture seule.
