# Vue globale (C4)

Modèle [C4](https://c4model.com) : on zoome du contexte vers les conteneurs, puis vers les composants des plus gros morceaux.

## Niveau 1 — Contexte

```mermaid
flowchart TB
  user([Habitant])
  jabfy[Jabfy<br/>assistant domestique local]
  devices[Appareils connectés<br/>Zigbee · MQTT · Modbus · HTTP]
  registry[Dépôts de modèles<br/>téléchargement initial uniquement]

  user -->|demande vocale ou texte| jabfy
  jabfy -->|réponse vocale ou texte| user
  jabfy -->|commandes vérifiées| devices
  devices -->|télémétrie, changements d'état| jabfy
  registry -.->|modèles| jabfy
```

Le seul échange avec l'extérieur est le téléchargement initial des modèles. Tout le reste se passe sur le réseau local.

## Niveau 2 — Conteneurs (architecture cible)

Un bloc par repo. Règle centrale : **l'IA propose, Guard autorise, le Bus exécute**.

```mermaid
flowchart LR
  subgraph clients[Clients]
    desktop[jabfy-desktop<br/>Electron + React]
    web[jabfy-web<br/>React]
    mobile[jabfy-mobile<br/>React Native]
    voice[jabfy-voice<br/>micro · STT · TTS]
  end
  core[jabfy-core<br/>FastAPI · raisonnement]
  llm[(Serveur de modèles<br/>Ollama / llama.cpp)]
  guard[jabfy-guard<br/>autorisation déterministe]
  bus[jabfy-bus<br/>bus JSON · exécution · audit]
  tts[jabfy-tts<br/>Kokoro-82M]
  mqtt[(Broker MQTT)]
  devices[Appareils réels]
  sim[jabfy-simulation<br/>maison virtuelle 3D]

  desktop -->|HTTP| core
  web -->|HTTP| core
  mobile -->|HTTP| core
  voice -->|texte| core
  core -->|API compatible OpenAI| llm
  core -->|réponse à lire| tts
  core -->|proposition d'action| bus
  bus -->|demande d'autorisation| guard
  bus <--> mqtt
  mqtt <--> devices
  mqtt <--> sim
```

| Repo | Rôle | Technologie | Doc composant |
|---|---|---|---|
| jabfy-core | Reçoit la demande, interroge le modèle, renvoie une proposition vérifiée | Python, FastAPI | ✅ |
| jabfy-bus | Traduit les protocoles en messages JSON communs, vérifie, exécute, audite | Python, bibliothèque standard | ✅ |
| jabfy-guard | Décide d'autoriser une commande : risques, politiques, refus par défaut | Python, bibliothèque | Code sur branche |
| jabfy-simulation | Maison virtuelle 3D qui parle de vrais protocoles | Python, FastAPI, Three.js | ✅ |
| jabfy-deploy | Assemble et lance la pile | Docker Compose | ✅ |
| jabfy-voice | Micro, transcription, réponse, voix | Python | ✅ (en PR) |
| jabfy-tts | Synthèse vocale locale | Rust (migration depuis TypeScript) | ✅ |
| jabfy-desktop, jabfy-web, jabfy-mobile | Interfaces utilisateur | Electron, React, React Native | Pas encore de code |

[jabfy-deploy](../composants/README.md) assemble ces conteneurs : il possède la topologie, les connexions, les volumes et les contrôles de santé.

## Ce qui tourne aujourd'hui : la V0.0.1

La V0.0.1 est une **maison virtuelle pilotée par l'IA**, lancée en une commande par jabfy-deploy. Elle diffère de la cible sur trois points :

- **Bus et Guard sont embarqués** dans le processus de la simulation, comme bibliothèques ([ADR-0006](adr/0006-bus-et-guard-embarques.md)) ;
- **la demande est tapée au clavier** dans l'interface 3D : la voix n'est pas encore branchée ;
- **rien n'est exécuté sans clic** : l'utilisateur voit la proposition et clique sur « Appliquer ».

```mermaid
flowchart LR
  browser([Navigateur<br/>127.0.0.1:8080])
  subgraph simc[conteneur jabfy-sim]
    ui[Interface 3D et panneau IA]
    busg[jabfy-bus + jabfy-guard<br/>embarqués]
  end
  core[conteneur core<br/>jabfy-core]
  ollama[(conteneur ollama<br/>qwen2.5:1.5b)]
  mqtt[(conteneur mosquitto)]

  browser --> ui
  ui -->|demande de proposition| core
  core -->|inventaire de la maison| ui
  core -->|API compatible OpenAI| ollama
  ui -->|« Appliquer »| busg
  busg <-->|MQTT, format Zigbee2MQTT| mqtt
```

### État de convergence vers `main`

La V0.0.1 se lance à partir de branches compatibles, listées dans la doc de jabfy-deploy. Leur fusion sur `main` est le chantier principal de la phase suivante.

| Repo | Branche V0.0.1 | Sur `main` ? |
|---|---|---|
| jabfy-bus | `bus-2-publish-container-image` | ✅ Fusionnée (PR #3 et #6) |
| jabfy-core | `core-3-publish-container-image` | ❌ `main` expose seulement `POST /act` |
| jabfy-guard | `guard-4-v001-deployment` | ❌ `main` ne contient pas encore la bibliothèque |
| jabfy-simulation | `sim-2-v001-deployment` | ❌ |
| jabfy-deploy | `deploy-1-bootstrap-container-deployment` | ❌ |

En parallèle, la branche `core-12-bus-integration` explore une autre option : **embarquer le bus dans Core** plutôt que dans la simulation. Les deux lignes doivent être réconciliées par une décision d'équipe, à consigner dans un ADR.

## Niveau 3 — Composants

### jabfy-bus

```mermaid
flowchart TB
  adapters[Protocol Adapters<br/>MQTT · HTTP · Zigbee2MQTT · Modbus TCP · CoAP] --> ubus[Universal JSON Bus<br/>messages v1.0, pub/sub interne]
  ubus --> verif[Verification Engine<br/>risque + politiques, ou authorizer Guard]
  verif --> exec[Execution Layer<br/>traducteurs par protocole, admission à usage unique]
  verif --> audit[Audit<br/>append-only, chaîne SHA-256, écrit avant envoi]
  exec --> audit
```

### jabfy-core (`main`)

```mermaid
flowchart LR
  api[api/routes_actions<br/>POST /act] --> orch[core/action_orchestrator]
  orch --> prompt[core/prompt_builder<br/>prompt + état des appareils]
  orch --> client[core/openai_client<br/>API compatible OpenAI]
  orch --> parser[core/action_parser<br/>extraction du JSON]
  orch --> verify[core/verification<br/>appareils connus, booléens]
```

### jabfy-simulation

```mermaid
flowchart LR
  ui3d[Interface 3D] -->|HTTP| app[dashboard/app.py<br/>FastAPI]
  app --> runtime[dashboard/runtime.py<br/>moteur et état]
  app -->|commande| busrunner[integration/bus_runner.py<br/>bus + guard + audit]
  busrunner --> emit[emitters/mqtt.py]
  emit <-->|Zigbee2MQTT| mq[(Mosquitto)]
  app -->|/api/ai/*| core[(jabfy-core)]
```

Le détail de chaque composant est dans [Composants](../composants/README.md).
