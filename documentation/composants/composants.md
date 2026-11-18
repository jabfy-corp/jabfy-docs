# Composants

Un dossier `composants/<repo>/` par repo, rempli de l'une de ces deux façons :

| Façon | Quand | Où modifier |
|---|---|---|
| **Recopié** depuis le `docs/` du repo (recommandé) | Le repo a un `docs/` sur `main` et figure dans [`composants.txt`](https://github.com/jabfy-corp/jabfy-docs/blob/main/composants.txt) | Dans le repo d'origine. Chaque page commence par un lien vers sa source. |
| **Écrit à la main** dans jabfy-docs | Le repo n'a pas encore de `docs/` | Directement dans `documentation/composants/<repo>/`, par PR sur jabfy-docs |

> Ne modifiez jamais une page recopiée, ni dans GitBook ni dans jabfy-docs : la synchronisation suivante écraserait la modification. Un dossier recopié contient un fichier `.synchro`.

Un dossier écrit à la main n'est jamais touché par la synchronisation. Quand le repo aura son propre `docs/`, déplacez-y les pages, supprimez le dossier écrit à la main, et la synchronisation prendra le relais.

## Fonctionnement

1. Un push sur `main` qui touche `docs/` dans un repo déclenche son workflow `notify-docs.yml`.
2. Ce workflow envoie un événement `docs-updated` à jabfy-docs.
3. Le workflow [`sync-composants.yml`](https://github.com/jabfy-corp/jabfy-docs/blob/main/.github/workflows/sync-composants.yml) clone le `docs/` de chaque repo listé dans [`composants.txt`](https://github.com/jabfy-corp/jabfy-docs/blob/main/composants.txt), lance [`scripts/sync_composants.py`](https://github.com/jabfy-corp/jabfy-docs/blob/main/scripts/sync_composants.py) et commite le résultat.
4. GitBook Git Sync publie le commit.

Le workflow tourne aussi chaque nuit et peut être lancé à la main (« Run workflow »), au cas où un événement aurait été perdu.

## Ce qui est publié

- Seuls les repos listés dans [`composants.txt`](https://github.com/jabfy-corp/jabfy-docs/blob/main/composants.txt) sont recopiés.
- Les fichiers et dossiers dont le nom commence par `_` ou `.` ne sont jamais recopiés : `docs/_interne/` sert à la doc qui doit rester privée.
- Les liens qui sortent de `docs/` (`../schemas/…`, `../README.md`) sont réécrits vers GitHub.
- Les pages suivent l'ordre dans lequel le `README.md` du composant les cite, puis l'ordre alphabétique.
- Si un repo ne peut pas être cloné (repo privé sans `DOCS_SYNC_TOKEN`), sa doc déjà publiée est conservée et les autres repos sont synchronisés normalement.

Un repo privé n'est ajouté qu'après le tri de sa doc : une fois agrégée, elle devient lisible sur le site.

## Lancer la synchronisation en local

```bash
mkdir -p _sources
for repo in $(sed -e 's/#.*//' composants.txt); do
  git clone --depth 1 "git@github.com:jabfy-corp/$repo.git" "_sources/$repo"
done
python3 scripts/sync_composants.py --sources _sources
```
