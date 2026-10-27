# Tests et validation

> ⚠️ Page recopiée automatiquement depuis [jabfy-deploy/docs/tests.md](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docs/tests.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Tests de Deploy

Depuis la racine du dépôt :

```bash
python3 -m venv .venv
.venv/bin/python -m pip install pytest PyYAML
.venv/bin/python -m pytest -q tests
docker compose -f compose.local.yml config --quiet
python3 scripts/start.py --check
```

Ces commandes ne démarrent aucun service. La dernière exige les quatre dépôts
frères compatibles ; la validation Compose seule ne vérifie pas leurs imports.

| Suite | Ce qui est vérifié |
|---|---|
| `tests/test_launcher.py` | Build et attente de santé, téléchargement optionnel, bon fichier Compose, arrêt sur erreur Docker ou source absente, absence de démarrage avec `--check` |
| `tests/test_compose.py` | Quatre services, chemins de build et de données, nom de projet stable, variables de connexion, contrôles de santé, ports limités à loopback |

La CI sur les PR vers `main` valide le YAML, lance ces tests et contrôle le format
du fichier de digests. Elle ne construit pas les images applicatives, ne télécharge
pas le modèle et ne teste pas une inférence réelle.

## Validation d'intégration

Une validation complète demande les cinq dépôts et un Docker fonctionnel : lancer
la procédure d'[Installation](installation.md), vérifier les quatre services sains,
le plan dans l'interface, les états MQTT et une proposition IA sans application
automatique. Consulter [Exploitation](exploitation.md) pour les commandes de diagnostic.

Les tests Python transversaux et le résultat historique du lancement du 9 octobre
2026 sont conservés dans le [guide V0.0.1](v0.0.1.md). Ce résultat historique ne
garantit pas les autres branches, d'autres machines ou des dépendances mises à jour.

## Vérification de la doc

Avant publication : vérifier les liens relatifs, le titre H1 de chaque page et
l'ordre des pages depuis [l'accueil](README.md). Tester la recopie avec
`scripts/sync_composants.py` de `jabfy-docs` dans une copie temporaire du site,
en n'injectant que la source Deploy pour ne pas régénérer les autres composants
depuis des branches locales non fusionnées.

Après fusion sur `main`, vérifier le résultat du workflow de notification, puis
le sommaire généré et le contrôle des liens du dépôt central. Un aperçu local
n'est pas une publication GitBook.
