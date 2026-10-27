# Interfaces et configuration

> ⚠️ Page recopiée automatiquement depuis [jabfy-deploy/docs/interfaces.md](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docs/interfaces.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

Deploy n'expose pas d'API applicative propre. Il configure les interfaces des services.

## Réseau de la stack locale

| Interface | Depuis la machine hôte | Dans le réseau Compose |
|---|---|---|
| Maison et interface web | `http://127.0.0.1:8080` | `http://jabfy-sim:8080` |
| MQTT | `127.0.0.1:1883` | `mosquitto:1883` |
| Core | Aucun port publié | `http://core:8000` |
| Ollama | Aucun port publié | `http://ollama:11434` |

Le port 1883 parle MQTT, pas HTTP : il ne s'ouvre pas comme une page web.
Les ports publiés sont liés à loopback. Ne pas remplacer cette restriction par
une exposition réseau pour ce prototype sans authentification.

## Variables modifiables via Compose

| Variable | Défaut | Effet |
|---|---|---|
| `SIM_PORT` | `8080` | Port hôte de l'interface |
| `MQTT_PORT` | `1883` | Port hôte de MQTT, sans changer le port interne |
| `JABFY_GUARD_MODE` | `normal` | `restricted` bloque les commandes |

Compose lit les variables du shell ou le fichier `.env` de Deploy, ignoré par Git.
Le lanceur affiche `SIM_PORT` depuis le shell uniquement : si le port est défini
seulement dans `.env`, son message final peut indiquer 8080. Le port effectivement
publié se vérifie avec `docker compose -f compose.local.yml ps`.

## Valeurs fixées dans compose.local.yml

| Service | Variable | Valeur |
|---|---|---|
| Core | `JABFY_LLM_BASE_URL` | `http://ollama:11434/v1` |
| Core | `JABFY_LLM_TIMEOUT_SECONDS` | `120` |
| Core | `JABFY_SIMULATION_URL` | `http://jabfy-sim:8080` |
| Simulation | `MQTT_BROKER` | `mosquitto:1883` |
| Simulation | `JABFY_CORE_URL` | `http://core:8000` |
| Ollama | `OLLAMA_NO_CLOUD` | `1` |

Ces valeurs sont littérales dans Compose : les définir dans `.env` ne les remplace
pas automatiquement. Un changement exige une modification explicite de la configuration.

## Contrats applicatifs utilisés

- Le navigateur appelle les routes `/api/…` de Simulation sur la même origine.
- Simulation appelle Core pour découvrir les modèles et proposer des actions.
- Core lit l'inventaire via `/api/ai/context` de Simulation et appelle l'API
  compatible OpenAI d'Ollama sous `/v1`.
- Bus et Guard communiquent dans le processus Simulation, pas via deux API réseau.

Les schémas et règles restent dans leurs dépôts applicatifs. Deploy ne duplique
pas les validations d'actions.
