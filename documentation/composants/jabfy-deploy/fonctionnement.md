# Fonctionnement interne

> ⚠️ Page recopiée automatiquement depuis [jabfy-deploy/docs/fonctionnement.md](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docs/fonctionnement.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Carte des fichiers

| Fichier | Responsabilité |
|---|---|
| [scripts/start.py](https://github.com/jabfy-corp/jabfy-deploy/blob/main/scripts/start.py) | Vérifications, build, démarrage, téléchargement du modèle |
| [compose.local.yml](https://github.com/jabfy-corp/jabfy-deploy/blob/main/compose.local.yml) | Topologie de la maison virtuelle V0.0.1 |
| [docker/mosquitto.conf](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docker/mosquitto.conf) | Broker MQTT local, accès anonyme sur le réseau de la stack |
| [docker-compose.yml](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docker-compose.yml) | Ancienne topologie fondée sur les images GHCR |
| [deployment.env](https://github.com/jabfy-corp/jabfy-deploy/blob/main/deployment.env) | Références d'images de cette ancienne topologie |
| [tests/](https://github.com/jabfy-corp/jabfy-deploy/blob/main/tests) | Contrats du lanceur et de Compose |

## Parcours du lanceur

1. Vérifier la présence de fichiers et marqueurs attendus dans les quatre dépôts frères.
2. Vérifier que Docker existe, puis exécuter `compose config --quiet`.
3. Avec `--check`, s'arrêter ici ; sinon vérifier l'accès au daemon via `docker info`.
4. Construire et démarrer avec `up --build -d --wait --wait-timeout 180`.
5. Sauf avec `--no-ai`, exécuter `ollama pull` pour le modèle choisi.
6. Afficher l'adresse de l'interface.

Le script utilise la bibliothèque standard Python et lance les commandes depuis
la racine de Deploy, quel que soit le dossier courant de l'appelant. En cas d'échec,
il retourne un code non nul et conserve les données ; il ne fait pas de rollback
et peut laisser certains services démarrés.

## Services et ordre de démarrage

| Service | Source | Contrôle de santé |
|---|---|---|
| `mosquitto` | Image `eclipse-mosquitto:2` | Publication MQTT locale |
| `ollama` | Image `ollama/ollama:latest` | `ollama list` |
| `core` | Dockerfile du dépôt Core | HTTP `/health` |
| `jabfy-sim` | Dockerfile de Simulation, contexte parent des dépôts | Simulation active, Guard actif, deux clients MQTT connectés |

Core démarre après le démarrage du conteneur Ollama, sans attendre son état sain.
Simulation attend que Core et Mosquitto soient sains. Le lanceur attend ensuite
la santé de l'ensemble. Un Core sain ou un `ollama list` réussi ne prouve ni la
présence d'un modèle ni la réussite d'une inférence.

Tous les services utilisent `restart: unless-stopped`. Un état `unhealthy` ne
redémarre pas à lui seul un processus encore vivant. Simulation dispose de
30 secondes pour s'arrêter proprement.

## Données et isolation

Le nom du projet Compose reste `jabfy-simulation` pour réutiliser les conteneurs
et volumes de la première version. Cela ne transfère pas l'orchestration au
simulateur : c'est bien Deploy qui définit et lance la stack.

Le plan et l'audit sont montés depuis `../jabfy-simulation/data` vers `/app/data`.
Le volume `ollama-models` conserve les modèles ; avec le nom de projet par défaut,
Docker le nomme `jabfy-simulation_ollama-models`.

Le build de Simulation embarque les bibliothèques Bus et Guard. Son
`Dockerfile.dockerignore` limite le contexte aux sources nécessaires : les maisons,
secrets et environnements virtuels ne doivent pas entrer dans l'image.
