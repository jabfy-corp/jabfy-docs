# jabfy-docs

Source du site de documentation de Jabfy, publié avec GitBook Git Sync.

| Chemin | Rôle |
|---|---|
| [`documentation/`](documentation/README.md) | Contenu du site : c'est le seul dossier synchronisé avec GitBook |
| [`documentation/SUMMARY.md`](documentation/SUMMARY.md) | Sommaire du site |
| `documentation/composants/` | Généré : copie du `docs/` de chaque repo, à ne pas modifier ici |
| [`composants.txt`](composants.txt) | Repos dont le `docs/` est recopié sur le site |
| [`scripts/sync_composants.py`](scripts/sync_composants.py) | Script de recopie, lancé par `.github/workflows/sync-composants.yml` |
| `gitbook-docs.yaml` | Structure du site GitBook, écrite par GitBook |

Pour contribuer : [documentation/contribuer/README.md](documentation/contribuer/README.md).
