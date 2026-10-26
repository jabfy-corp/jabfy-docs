# Contribuer à la doc

Tout le monde contribue par **pull request sur GitHub**. Le compte GitBook sert à publier, pas à rédiger.

## Où écrire quoi

| Contenu | Où | Comment |
|---|---|---|
| Vision, veille, architecture globale, ADR, protection, performance, suivi | jabfy-docs | PR sur jabfy-docs |
| Installation, fonctionnement interne, interfaces d'un composant | `docs/` du repo concerné (recommandé) | PR sur ce repo ; la page apparaît dans [Composants](../composants/README.md) après la synchronisation |
| Doc d'un composant dont le repo n'a pas encore de `docs/` | `documentation/composants/<repo>/` dans jabfy-docs | PR sur jabfy-docs |
| Ce qui doit rester privé | `docs/_interne/` du repo concerné | Jamais recopié sur le site |

> Une page **recopiée** dans [Composants](../composants/README.md) se modifie dans son repo d'origine, jamais dans GitBook ni dans jabfy-docs : la synchronisation suivante écraserait la modification.

## Ajouter une page à jabfy-docs

1. Créer le fichier dans le bon dossier, en partant du modèle de la section s'il y en a un.
2. L'ajouter dans [`SUMMARY.md`](../SUMMARY.md) : une page absente du sommaire n'apparaît pas dans GitBook.
3. Ouvrir une PR liée à une issue (`Closes #N`), comme dans tous les repos.

La CI vérifie que les liens internes ne sont pas cassés.

## Modèles

| Pour | Modèle |
|---|---|
| Une fiche de veille | [veille/modele.md](../veille/modele.md) |
| Une décision d'architecture | [architecture/adr/modele.md](../architecture/adr/modele.md) |
| Une métrique | [performance/modele.md](../performance/modele.md) |
| Un compte-rendu de RDV | [suivi/modele-rdv.md](../suivi/modele-rdv.md) |
| La doc d'un repo | [Écrire la doc d'un repo](ecrire-la-doc.md) |

Voir aussi les [conventions Git](conventions-git.md).
