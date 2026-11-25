# Deploy V1 — exploitation locale et tests

> ⚠️ Page recopiée automatiquement depuis [jabfy-deploy/docs/deploy-v1.md](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docs/deploy-v1.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Démarrer

Utiliser Git, Python 3.9+ et Docker avec Compose v2 et la prise en charge de
`up --wait`. Depuis la racine de Deploy :

```sh
python3 scripts/deploy.py config
python3 scripts/deploy.py up
python3 scripts/deploy.py model
```

`config` imprime le document Compose résolu en JSON. `up` lit
[sources.lock.json](https://github.com/jabfy-corp/jabfy-deploy/blob/main/sources.lock.json), récupère chaque commit dans un clone
temporaire et construit les images. Lorsqu'un dépôt frère contient le commit,
Git lit ses objets locaux. Sinon, Git utilise SSH vers `jabfy-corp` et demande
un accès en lecture aux dépôts concernés. Les modifications non commitées et les
données de travail des dépôts frères sont exclues de la construction.

Le lanceur attend que les quatre services soient sains et affiche l'adresse de
l'interface. Par défaut, ouvrir http://127.0.0.1:8080. MQTT écoute sur le port
local 1883. Si une autre instance utilise ces ports, exporter par exemple
`SIM_PORT=8082` et `MQTT_PORT=1884` avant le lancement.

La commande `model` télécharge `qwen2.5:1.5b` dans Ollama. Elle accepte
`--model NOM`. Les contrôles manuels sont utilisables dès la fin de `up`.
Les synthèses et entrées vocales sont hors du périmètre de ce déploiement.

## Exploiter et mettre à jour

```sh
python3 scripts/deploy.py status
python3 scripts/deploy.py logs
python3 scripts/deploy.py down
```

Le projet Compose par défaut est `jabfy-v1`. Il possède ses propres volumes nommés
`home` (plan et audit) et `ollama-models`. Au premier lancement il crée une maison
neuve. `down` conserve les volumes. `COMPOSE_PROJECT_NAME` permet de choisir une
instance distincte ; conserver la même valeur pour toutes les commandes de cette instance.

Pour changer une version applicative, modifier le SHA complet du composant,
relancer le test Docker puis `up`. Les deux images d'infrastructure sont fixées
par digest dans [compose.v1.yml](https://github.com/jabfy-corp/jabfy-deploy/blob/main/compose.v1.yml). Les Dockerfiles applicatifs
résolvent encore leur image Python et des dépendances au build. Le verrou porte
sur les sources et les images d'infrastructure, pas sur chaque dépendance transitive.
Un échec retourne un code non nul ; après un démarrage partiel, `status` et `logs`
permettent de diagnostiquer, puis `up` de réessayer.

## Tests reproductibles

```sh
python3 -m venv .venv
.venv/bin/python -m pip install pytest PyYAML
.venv/bin/python -m pytest -q tests
JABFY_E2E=1 .venv/bin/python -m pytest -q tests/test_v1.py
JABFY_E2E=1 JABFY_E2E_MODEL=1 .venv/bin/python -m pytest -q tests/test_v1.py
```

La suite rapide vérifie notamment le résultat réel de `docker compose config` avec
le plugin Compose installé. Le test d'intégration demande un daemon actif et les
sources accessibles. Il utilise un projet à identifiant aléatoire, deux ports
dynamiques sur loopback et des volumes réservés au test. Il vérifie l'inventaire
vu par Core, une commande de lampe et son état remonté, la persistance d'une
maison renommée après recréation et le refus d'une commande en mode restreint.
Le mode modèle ajoute un téléchargement et une inférence sur CPU. Le test nettoie
ses conteneurs, ses volumes et ses images applicatives à la fin.

## Automatisation existante

La CI sur PR vérifie le YAML, lance pytest, résout le Compose historique local et
contrôle le format de `deployment.env`. Ce fichier GHCR contient encore cinq
digests provisoires acceptés par la CI. Le workflow `update-image-digest` propose
une PR de mise à jour du verrou GHCR. La notification documentaire et le contrôle
du lien PR–issue sont des workflows séparés. Le lanceur V1 et les tests s'exécutent
depuis un terminal et peuvent être appelés par un futur pipeline.
