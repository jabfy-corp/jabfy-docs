# Contribuer à la doc

Tout le monde contribue par **pull request sur GitHub**. GitBook ne fait qu'afficher : personne n'écrit dedans, et tout ce qui est fusionné sur `main` est publié une minute plus tard.

## Où écrire quoi

| Contenu | Où | Publication |
|---|---|---|
| Veille, architecture, ADR, protection, performance, projet, suivi | `documentation/` de jabfy-docs | Après fusion de la PR sur jabfy-docs |
| Doc technique d'un composant (installation, fonctionnement, interfaces, tests) | `docs/` du repo concerné (recommandé) | Recopiée chaque nuit dans [Composants](../composants/README.md), après fusion sur `main` du repo |
| Doc d'un composant dont le repo n'a pas encore de `docs/` | `documentation/composants/<repo>/` dans jabfy-docs | Après fusion de la PR sur jabfy-docs |
| Ce qui doit rester privé | `docs/_interne/` du repo concerné | Jamais |

> Une page **recopiée** dans [Composants](../composants/README.md) se modifie dans son repo d'origine, jamais dans GitBook ni dans jabfy-docs : la synchronisation suivante écraserait la modification.

## Ajouter une trouvaille

| Vous avez trouvé… | Vous écrivez dans… |
|---|---|
| Une solution, un benchmark, un article utile | `documentation/veille/<sujet>.md` : le tableau comparatif, avec la date et la source |
| Une décision prise en équipe | Un nouvel ADR, à partir de [`architecture/adr/modele.md`](../architecture/adr/modele.md) |
| Une mesure (latence, WER, mémoire…) | `documentation/performance/<métrique>.md`, tableau « Résultats », et le script dans `benchmarks/` |
| Une information juridique (INPI, EPITECH, licence) | `documentation/protection/…` |
| Un compte-rendu de RDV | `documentation/suivi/AAAA-MM-JJ.md`, à partir du [modèle](../suivi/modele-rdv.md) |

## Modifier une page depuis GitHub, sans rien installer

1. **Créer une issue** dans jabfy-docs, par exemple « [Docs] Veille STT : comparatif Whisper / Vosk ».
2. **Ouvrir la page** sur GitHub, par exemple `documentation/veille/stt.md`.
3. Cliquer sur le **crayon** (« Edit this file »), modifier le texte, vérifier le rendu dans l'onglet « Preview ».
4. **Commit changes…** → « Create a new branch for this commit and start a pull request ». Nom de branche : `docs-<n°issue>-<sujet>`.
5. Dans la PR, écrire **`Closes #<n°issue>`**, puis la faire relire par un autre membre avant de la fusionner.

## Ajouter une page

1. Créer le fichier dans le bon dossier, en partant du modèle de la section.
2. **L'ajouter dans [`SUMMARY.md`](../SUMMARY.md)** : une page absente du sommaire n'apparaît pas sur le site.
3. Images : à côté de la page, avec un lien relatif (`![schéma](schema-stt.png)`). Diagrammes : en Mermaid.

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
