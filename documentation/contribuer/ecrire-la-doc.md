# Écrire la doc d'un repo

Chaque repo a un `README.md` et un dossier `docs/`. Le `docs/` est recopié automatiquement dans [Composants](../composants/README.md) chaque nuit, dès qu'il est sur `main`.

## Structure

Tous les composants suivent le même plan, pour qu'un lecteur s'y retrouve d'un repo à l'autre :

```
README.md             # présentation courte, démarrage rapide, lien vers docs/
docs/
├── README.md         # rôle dans l'architecture, liste des pages, état actuel, limites et TODO
├── installation.md   # prérequis, installation, configuration, lancement
├── fonctionnement.md # architecture interne, flux, choix d'implémentation
├── interfaces.md     # ce que le composant expose et consomme (API, messages du bus)
├── tests.md          # lancer les tests, ce qu'ils couvrent, CI
├── code/             # facultatif : une page par fichier source (carte du code)
└── _interne/         # jamais publié : failles, notes privées
```

Exemples complets : jabfy-bus, jabfy-core, jabfy-simulation, jabfy-deploy et jabfy-tts, dans [Composants](../composants/README.md).

Tout fichier ou dossier dont le nom commence par `_` ou `.` reste dans le repo et n'est pas publié.

## Règles

- **Une page = un sujet.** Mieux vaut trois pages courtes qu'une longue.
- **Le premier titre `#` est le titre de la page** : il apparaît dans le sommaire du site.
- **L'ordre des pages dans le menu** suit l'ordre dans lequel `docs/README.md` les cite.
- **Liens relatifs** entre pages de `docs/` (`[Installation](installation.md)`). Les liens qui sortent de `docs/` (`../schemas/…`) sont réécrits vers GitHub par la synchronisation.
- **Images** à côté des pages, dans `docs/`, avec un lien relatif. **Diagrammes en Mermaid.**
- **Exemples exécutables** : une commande ou un extrait de code montré dans la doc doit fonctionner tel quel.
- **État honnête** : la section « Limites connues et TODO » dit ce qui ne marche pas encore. C'est ce qui rend la doc crédible.
- **À jour avec le code** : une PR qui change un comportement documenté met la doc à jour dans la même PR.

## Ajouter un repo au site

1. Créer son `docs/` en suivant la structure ci-dessus, et le fusionner sur `main`.
2. Vérifier que le repo est listé dans `composants.txt` de jabfy-docs.
3. **Repo privé** : vérifier que le token `DOCS_SYNC_TOKEN` de jabfy-docs a accès à ce repo (en lecture seule). Sa doc devient lisible sur le site : ce qui doit rester privé va dans `docs/_interne/`.
4. Pour une publication immédiate plutôt que nocturne : copier `.github/workflows/notify-docs.yml` depuis jabfy-template et créer le secret `DOCS_DISPATCH_TOKEN` **dans le repo**, car sur le plan GitHub gratuit, les secrets d'organisation ne sont pas accessibles aux repos privés.

Sans attendre la nuit, la synchronisation se lance à la main : jabfy-docs → Actions → « Sync composants » → « Run workflow ».
