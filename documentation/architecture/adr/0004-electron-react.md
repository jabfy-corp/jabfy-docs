# ADR-0004 — Electron et React pour le client desktop

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Proposé (rétroactif) | | | |

> Décision déjà appliquée, consignée après coup. Contexte et options à compléter par l'équipe avant de passer en « Accepté ».

## Contexte

jabfy-desktop est le client principal : il enveloppe jabfy-core. Le client web (jabfy-web) est aussi en React + TypeScript + Vite, et le mobile (jabfy-mobile) en React Native. Le prototype était déjà en Electron + React.

## Options étudiées

1. **Electron + React + TypeScript (Vite)** — même langage et mêmes composants que le client web, écosystème connu de l'équipe.
2. **Tauri** — à compléter.
3. **Application native** — à compléter.

## Décision

Le client desktop est une application Electron avec une interface React + TypeScript, construite avec Vite.

## Conséquences

- Le code d'interface peut être partagé avec jabfy-web.
- L'empreinte mémoire d'Electron compte dans le budget RAM de la machine cible : à mesurer dans [Performance › CPU et RAM](../../performance/ressources.md).
- À compléter.
