# jabfy-docs

Source du site de documentation de Jabfy, publié avec GitBook Git Sync.

**📖 Lire la doc : https://jabfy-corp.gitbook.io/jabfy-corp-docs/**

> Site public depuis le 18/11/2026 (offre GitBook gratuite) : tout ce qui est fusionné sur `main` est visible par tout le monde et indexé par les moteurs de recherche. N'y mettez ni secret, ni donnée personnelle.

| Chemin | Rôle |
|---|---|
| [`documentation/`](documentation/README.md) | Contenu du site : c'est le seul dossier synchronisé avec GitBook |
| [`documentation/SUMMARY.md`](documentation/SUMMARY.md) | Sommaire du site |
| `documentation/composants/` | Un dossier par repo : recopié depuis son `docs/` (contient `.synchro`, ne pas modifier ici) ou écrit à la main |
| [`composants.txt`](composants.txt) | Repos dont le `docs/` est recopié sur le site |
| [`scripts/sync_composants.py`](scripts/sync_composants.py) | Script de recopie, lancé par `.github/workflows/sync-composants.yml` |
| `gitbook-docs.yaml` | Structure du site GitBook, écrite par GitBook |

Pour contribuer : [documentation/contribuer/README.md](documentation/contribuer/README.md).
