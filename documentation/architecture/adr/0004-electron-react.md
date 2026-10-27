# ADR-0004 — Electron et React pour le client desktop

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté (consigné a posteriori) | 27/10/2026 | Équipe | — |

## Contexte

jabfy-desktop sera le client principal sur ordinateur. Le client web (jabfy-web) est en React + TypeScript, le mobile (jabfy-mobile) en React Native, et le premier prototype de Jabfy était déjà en Electron + React. Les clients ne font qu'afficher et envoyer des demandes à jabfy-core : ils ne portent aucune logique de décision.

## Options étudiées

1. **Electron + React + TypeScript (Vite)** — même langage et mêmes composants que le client web, technologie déjà utilisée dans le prototype.
2. **Tauri** — application beaucoup plus légère (moteur web du système, cœur en Rust), mais une pile de plus à apprendre.
3. **Application native** par système — meilleure intégration, mais trois bases de code.

## Décision

Le client desktop est une application **Electron**, avec une interface **React + TypeScript** construite avec Vite. Le squelette est en place dans jabfy-desktop.

## Conséquences

- Le code d'interface peut être partagé avec jabfy-web, et en partie avec jabfy-mobile.
- Electron embarque son propre navigateur : son empreinte mémoire compte dans le budget de la machine cible ([Ressources](../../performance/ressources.md)).
- À réévaluer face à Tauri si l'application desktop doit tourner sur la même box que le modèle de langage.
