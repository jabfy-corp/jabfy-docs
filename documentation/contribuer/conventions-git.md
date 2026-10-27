# Conventions Git

Reprend le `CONTRIBUTING.md` de [jabfy-template](https://github.com/jabfy-corp/jabfy-template), commun à tous les repos.

## Avant de commencer

Toute contribution part d'une issue. S'il n'y en a pas, en ouvrir une avec le modèle adapté.

## Nom des branches

```
<repo>-<numéro-issue>-<description-courte>
```

Exemple : `tts-1-wiki-documentation`.

| Repo | Préfixe |
|---|---|
| jabfy-core | `core` |
| jabfy-bus | `bus` |
| jabfy-guard | `guard` |
| jabfy-simulation | `sim` |
| jabfy-deploy | `deploy` |
| jabfy-voice | `voice` |
| jabfy-tts | `tts` |
| jabfy-desktop | `desktop` |
| jabfy-web | `web` |
| jabfy-mobile | `mobile` |
| jabfy-prototype | `proto` |
| jabfy-docs | `docs` |

## Messages de commit

```
<type>: <description>
```

| Type | Usage |
|---|---|
| `feat` | Nouvelle fonctionnalité ou prototype |
| `fix` | Correction de bug |
| `chore` | Maintenance, outillage, CI |
| `docs` | Documentation seule |
| `refactor` | Refactorisation sans changement de comportement |
| `test` | Tests seuls |

Exemple : `docs: add wake word benchmark page`.

## Pull requests

- Mettre `Closes #<numéro>` dans la description : une PR sans issue liée échoue à la validation. Le lien ne fonctionne que pour une PR qui vise la branche par défaut (`main`).
- Faire relire la PR par un autre membre avant de la fusionner : le relecteur de chaque repo est indiqué dans [Équipe](../projet/equipe.md).
- Ne pas renommer une branche qui a une PR ouverte : GitHub ferme la PR.

## Commits automatiques

Deux robots écrivent directement sur `main` de jabfy-docs, sans issue : la synchronisation des composants (« docs: sync composants ») et GitBook (« GitBook: … »). C'est normal.

## Releases

- Tag : `Année.MoisJour.Version`, la version commençant à 0. Exemple : `2026.324.0`.
- Titre : `Tag-Statut`, avec le statut `pre-release` ou `beta`. Une release stable a le tag seul pour titre.
