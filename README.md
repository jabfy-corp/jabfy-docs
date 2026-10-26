# jabfy-docs

Source du site de documentation de Jabfy, publié avec GitBook Git Sync.

**📖 Lire la doc : https://jabfy-corp.gitbook.io/jabfy-corp-docs/HyvaLxyexEdtkolJz8ZR/**

> Lien de partage privé : toute personne qui l'a peut lire le site. Ne le copiez pas dans un repo public ni en dehors de l'équipe.

| Chemin | Rôle |
|---|---|
| [`documentation/`](documentation/README.md) | Contenu du site : c'est le seul dossier synchronisé avec GitBook |
| [`documentation/SUMMARY.md`](documentation/SUMMARY.md) | Sommaire du site |
| `documentation/composants/` | Un dossier par repo : recopié depuis son `docs/` (contient `.synchro`, ne pas modifier ici) ou écrit à la main |
| [`composants.txt`](composants.txt) | Repos dont le `docs/` est recopié sur le site |
| [`scripts/sync_composants.py`](scripts/sync_composants.py) | Script de recopie, lancé par `.github/workflows/sync-composants.yml` |
| `gitbook-docs.yaml` | Structure du site GitBook, écrite par GitBook |

Pour contribuer : [documentation/contribuer/README.md](documentation/contribuer/README.md).
