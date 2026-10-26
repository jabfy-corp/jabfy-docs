# Installation et lancement

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/installation.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/installation.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Prérequis

- Python 3.10 ou plus récent. La CI teste 3.10, 3.11 et 3.12.
- Aucune dépendance pour le cœur : bibliothèque standard uniquement.

## Installation

```bash
pip install .            # cœur seul
pip install ".[api]"     # + API HTTP/WebSocket
pip install ".[all]"     # tous les extras
make dev                 # installation éditable avec tous les extras
```

| Extra | Apporte | Nécessaire pour |
|---|---|---|
| `mqtt` | `paho-mqtt` ≥ 2.0 | un vrai client MQTT |
| `api` | `fastapi`, `uvicorn` | `jabfy-bus serve` et les tests d'API |
| `modbus` | `pymodbus` ≥ 3.6 | un vrai client Modbus TCP |
| `yaml` | `PyYAML` | une configuration en `.yaml` |

## Commandes

```bash
jabfy-bus demo --steps 10                 # scénario mouvement → lampe en simulation
jabfy-bus demo --steps 10 --audit a.jsonl # idem, en gardant le journal d'audit
jabfy-bus validate message.json           # valide un message contre le schéma v1.0
jabfy-bus audit-verify audit.jsonl        # vérifie la chaîne d'un journal d'audit
jabfy-bus serve --config config.yaml      # API de consultation HTTP + WebSocket (extra api)
```

Options communes : `--log-level`, `--log-json` (logs en JSON lines), `--version`. Sans installation, remplacer `jabfy-bus` par `python3 -m jabfy_bus.cli`.

La démo n'a besoin d'aucune dépendance. Elle renvoie un code d'erreur si la lampe ne s'allume pas :

```text
$ jabfy-bus demo --steps 10
ticks           : 10
entities        : 3
decisions       : 1
executed        : 1
lamp state      : ON
audit records   : 4
audit verified  : True
```

## Configuration

Fichier JSON, ou YAML avec l'extra `yaml`. Exemple complet : [`examples/config.example.yaml`](https://github.com/jabfy-corp/jabfy-bus/blob/main/examples/config.example.yaml).

| Clé | Défaut | Rôle |
|---|---|---|
| `history_size` | `500` | Nombre de messages gardés en mémoire pour `/bus/history` |
| `audit_path` | aucun (en mémoire) | Fichier du journal d'audit (JSON Lines) |
| `api.host` | `127.0.0.1` | Adresse d'écoute de l'API |
| `api.port` | `8080` | Port de l'API |
| `api.allowed_origins` | `["http://localhost:5173"]` | Origines navigateur acceptées (CORS et WebSocket) |
| `adapters[]` | `[]` | `type`, `name`, `mode` (`read_only` par défaut), `options` |
| `policies[]` | `[]` | Règles de vérification : voir [Sécurité](security.md) |

> Aujourd'hui, `serve` ne lit que `history_size`, `audit_path` et `api`. Les sections `adapters` et `policies` sont validées au chargement, mais rien ne les démarre encore.

Sans `--config`, l'adresse et le port viennent de `JABFY_BUS_HOST` (défaut `127.0.0.1`) et `JABFY_BUS_PORT` (défaut `8080`).

## Conteneur

Le [`Dockerfile`](https://github.com/jabfy-corp/jabfy-bus/blob/main/Dockerfile) part de `python:3.12-slim`, installe l'extra `api`, tourne sous un utilisateur non root et lance `jabfy-bus serve` sur `0.0.0.0:8080`.

```bash
docker build -t jabfy-bus .
docker run --rm -p 8080:8080 jabfy-bus
```

Le workflow `publish-image.yml` publie l'image sur `ghcr.io/jabfy-corp/jabfy-bus` à chaque push sur `main` et à chaque release, puis prévient jabfy-deploy du nouveau digest si le secret `JABFY_DEPLOY_DISPATCH_TOKEN` est configuré. L'attestation de l'image n'est faite que si le repo est public : pour un repo privé, elle demande un plan GitHub Enterprise.

## Dans la V0.0.1

Le bus ne se lance pas seul : il est embarqué par jabfy-simulation, et toute la pile démarre depuis jabfy-deploy (`python3 scripts/start.py`). L'intégration côté code est décrite dans [Interfaces](interfaces.md).

## Commandes de développement

| Commande | Effet |
|---|---|
| `make test` | Lance les tests : voir [Tests](tests.md) |
| `make demo` | Lance la démo |
| `make lint` | `ruff check`, à titre indicatif (ne fait jamais échouer) |
| `make clean` | Supprime les fichiers de build et les caches |
