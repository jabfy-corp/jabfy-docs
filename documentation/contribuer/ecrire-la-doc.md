# Écrire la doc d'un repo

Chaque repo a un `README.md` et un dossier `docs/`, créés par [jabfy-template](https://github.com/jabfy-corp/jabfy-template). Le `docs/` est recopié automatiquement dans [Composants](../composants/README.md).

## Structure

```
README.md             # présentation courte, démarrage rapide, lien vers docs/
docs/
├── README.md         # page d'accueil du composant sur le site
├── installation.md   # prérequis, installation, configuration, lancement
├── fonctionnement.md # architecture interne, flux, choix d'implémentation
├── interfaces.md     # ce que le composant expose et consomme
└── _interne/         # jamais publié : failles, notes privées
```

Ajouter d'autres pages si besoin. Tout fichier ou dossier dont le nom commence par `_` ou `.` reste dans le repo et n'est pas publié.

## Règles

- **Une page = un sujet.** Mieux vaut trois pages courtes qu'une longue.
- **Le premier titre `#` est le titre de la page** : il apparaît dans le sommaire du site.
- **Liens relatifs** entre pages de `docs/` (`[Installation](installation.md)`). Les liens qui sortent de `docs/` (`../schemas/…`) sont réécrits vers GitHub par la synchronisation.
- **Images** à côté des pages, dans `docs/`, avec un lien relatif.
- **Diagrammes en Mermaid**, dans un bloc de code `mermaid`.
- **Exemples exécutables** : une commande montrée dans la doc doit fonctionner telle quelle.
- **À jour avec le code** : une PR qui change un comportement documenté met la doc à jour dans la même PR.
- La doc des repos privés n'est publiée qu'une fois le repo ajouté à `composants.txt` dans jabfy-docs : voir [Protection](../protection/README.md).

## Ajouter un repo existant au site

1. Créer son `docs/` en suivant la structure ci-dessus.
2. Copier `.github/workflows/notify-docs.yml` depuis jabfy-template.
3. Ajouter le repo à `composants.txt` dans jabfy-docs.
