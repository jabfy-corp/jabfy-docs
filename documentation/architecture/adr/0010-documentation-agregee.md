# ADR-0010 — Un site de documentation unique, alimenté par chaque repo

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté | 24/10/2026 | Elias | — |

## Contexte

Le projet compte une douzaine de repos. La doc technique doit rester à côté du code pour être tenue à jour, mais le suivi EIP demande une vue d'ensemble : vision, veille, architecture, objectifs, comptes-rendus. L'offre gratuite de GitBook ne compte qu'un seul éditeur, et ses « sections » par repo sont payantes.

## Options étudiées

1. **Une section GitBook par repo** — chaque repo synchronisé séparément, mais réservé aux offres payantes.
2. **Toute la doc dans un repo central** — simple, mais la doc technique s'éloigne du code et se périme.
3. **Un repo central (jabfy-docs) qui recopie automatiquement le `docs/` de chaque repo** — un seul site, la doc technique reste dans son repo.

## Décision

Option 3. jabfy-docs contient les pages communes et la section Composants, recopiée chaque nuit depuis le `docs/` de chaque repo par un workflow GitHub Actions. GitBook n'affiche que jabfy-docs, synchronisé par Git Sync. Toute l'équipe contribue par pull request sur GitHub.

## Conséquences

- Un seul compte GitBook suffit ; personne n'écrit dans GitBook.
- Une page de composant se modifie dans son repo d'origine, jamais dans jabfy-docs : la synchronisation l'écraserait.
- La lecture des repos privés demande un token en lecture seule (`DOCS_SYNC_TOKEN`), et leur doc devient lisible sur le site : ce qui doit rester privé va dans `docs/_interne/`.
