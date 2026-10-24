# Composants

Cette section est **générée automatiquement**. Chaque sous-dossier `composants/<repo>/` est une copie du dossier `docs/` du repo correspondant.

> Ne modifiez rien ici, ni dans GitBook ni dans ce repo : la synchronisation suivante écraserait la modification. Corrigez la page dans son repo d'origine ; chaque page copiée commence par un lien vers sa source.

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

Un repo privé n'est ajouté qu'après le tri de sa doc : une fois agrégée, elle devient lisible sur le site.

## Lancer la synchronisation en local

```bash
mkdir -p _sources
for repo in $(sed -e 's/#.*//' composants.txt); do
  git clone --depth 1 "git@github.com:jabfy-corp/$repo.git" "_sources/$repo"
done
python3 scripts/sync_composants.py --sources _sources
```
