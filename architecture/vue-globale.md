# Vue globale (C4)

Modèle [C4](https://c4model.com) : on zoome du contexte vers les conteneurs, puis vers les composants des plus gros morceaux.

## Niveau 1 — Contexte

```mermaid
flowchart TB
  user([Habitant])
  jabfy[Jabfy<br/>assistant domestique local]
  devices[Appareils connectés<br/>Zigbee · MQTT · Modbus · HTTP · CoAP]
  registry[Dépôts de modèles<br/>téléchargement initial uniquement]

  user -->|demande vocale ou texte| jabfy
  jabfy -->|réponse vocale ou texte| user
  jabfy -->|commandes vérifiées| devices
  devices -->|télémétrie, changements d'état| jabfy
  registry -.->|modèles| jabfy
```

Le seul échange avec l'extérieur est le téléchargement initial des modèles. Tout le reste reste sur le réseau local.

## Niveau 2 — Conteneurs (architecture cible)

Un bloc par repo.

```mermaid
flowchart LR
  subgraph clients[Clients]
    desktop[jabfy-desktop<br/>Electron + React]
    web[jabfy-web<br/>React]
    mobile[jabfy-mobile<br/>React Native + Expo]
  end
  subgraph voix[Voix]
    voice[jabfy-voice<br/>micro · STT · TTS]
    tts[jabfy-tts<br/>paquet npm Kokoro]
  end
  core[jabfy-core<br/>FastAPI · raisonnement · validation]
  llm[(Serveur de modèles<br/>Ollama / llama.cpp)]
  bus[jabfy-bus<br/>bus JSON · vérification · exécution · audit]
  guard[jabfy-guard<br/>bibliothèque d'autorisation]
  mqtt[(Broker MQTT)]
  sim[jabfy-simulation<br/>maison virtuelle 3D]
  devices[Appareils réels]

  desktop -->|HTTP| core
  web -->|HTTP| core
  mobile -->|HTTP| core
  voice -->|texte| core
  core -->|API compatible OpenAI| llm
  core -->|propositions d'action| bus
  bus -->|évaluation| guard
  bus <--> mqtt
  mqtt <--> sim
  mqtt <--> devices
```

[jabfy-deploy](https://github.com/jabfy-corp/jabfy-deploy) assemble ces conteneurs : il possède la topologie, les connexions, les volumes et les contrôles de santé.

## Déploiement V0.0.1

Ce que jabfy-deploy lance aujourd'hui, différent de la cible sur un point : **Bus et Guard sont embarqués dans le runtime de simulation**, et non des services séparés.

```mermaid
flowchart LR
  browser([Navigateur<br/>localhost:8080])
  subgraph simc[conteneur jabfy-sim]
    ui[Interface 3D et éditeur]
    bus[jabfy-bus embarqué]
    guard[jabfy-guard]
  end
  core[conteneur core<br/>jabfy-core]
  ollama[(conteneur ollama)]
  mqtt[(conteneur mosquitto)]

  browser --> ui
  ui -->|demande IA| core
  core -->|API compatible OpenAI| ollama
  core -->|propositions validées| ui
  ui --> bus
  bus -->|évaluation| guard
  bus <-->|MQTT, format Zigbee2MQTT| mqtt
```

Seuls des appareils virtuels sont pilotés.

## Niveau 3 — Composants

### jabfy-bus

```mermaid
flowchart TB
  ingest[Data Ingestion Layer] --> adapters[Protocol Adapters<br/>MQTT · HTTP · Zigbee2MQTT · Modbus TCP · CoAP]
  adapters --> ubus[Universal JSON Bus<br/>messages v1.0, pub/sub interne]
  ubus --> reasoning[Reasoning Engine<br/>propose des command.requested]
  reasoning --> verif[Verification Engine<br/>risque + politiques, refus par défaut]
  verif --> exec[Execution Layer<br/>traducteurs par protocole]
  exec --> audit[Audit Logs<br/>append-only, chaînage SHA-256]
```

### jabfy-core

```mermaid
flowchart LR
  api[app/api<br/>routes HTTP] --> orch[app/core<br/>backends de modèles, prompts, parsing, vérification]
  orch --> schemas[app/schemas<br/>contrats API et bus]
  orch --> simu[app/simulation<br/>inventaire et propositions]
```

Le détail de chaque composant est dans [Composants](../composants/README.md).
