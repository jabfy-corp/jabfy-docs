# Flux d'une demande

## Aujourd'hui (V0.0.1) : demande texte dans la maison virtuelle

```mermaid
sequenceDiagram
  autonumber
  actor U as Utilisateur
  participant S as jabfy-simulation
  participant C as jabfy-core
  participant L as Ollama
  participant G as jabfy-guard
  participant B as jabfy-bus
  participant M as Mosquitto

  U->>S: tape une consigne dans le panneau IA
  S->>C: demande de proposition (modèle, consigne)
  C->>S: GET /api/ai/context (inventaire de la maison)
  S-->>C: pièces, appareils, états
  C->>L: prompt + inventaire
  L-->>C: proposition en JSON
  C->>C: extraction et validation du JSON
  C-->>S: proposition validée
  S-->>U: affiche la proposition
  U->>S: clique sur « Appliquer »
  S->>B: command.requested
  B->>G: authorizer : autoriser la commande ?
  G-->>B: allow ou deny
  B->>B: écrit l'audit, avant tout envoi
  B->>M: publication sur zigbee2mqtt/[appareil]/set
  M-->>S: nouvel état de l'appareil virtuel
  S-->>U: mise à jour de la scène 3D
```

Points importants :

* **aucune proposition n'est exécutée automatiquement** : l'utilisateur garde la main ;
* **les commandes manuelles** (clic sur un appareil dans la scène 3D) suivent le même chemin Guard → Bus → audit ;
* **si l'écriture de l'audit échoue, la commande n'est pas envoyée**.

## Cible : du mot d'activation à la réponse vocale

```mermaid
sequenceDiagram
  autonumber
  actor U as Habitant
  participant V as jabfy-voice
  participant C as jabfy-core
  participant L as Modèle local
  participant G as jabfy-guard
  participant B as jabfy-bus
  participant D as Appareil
  participant T as jabfy-tts

  U->>V: « Jabfy, allume le salon »
  Note over V: wake word, puis enregistrement jusqu'au silence
  V->>V: transcription (faster-whisper)
  V->>C: demande en texte
  C->>L: prompt + inventaire
  L-->>C: proposition JSON
  C->>B: command.requested
  B->>G: évaluation (risque, politiques, contexte)
  G-->>B: allow ou deny
  B->>B: audit, avant tout envoi
  B->>D: commande dans le protocole de l'appareil
  D-->>B: nouvel état
  B-->>C: command.executed ou command.rejected
  C->>T: réponse en texte
  T->>U: voix, phrase par phrase
```

Ce qui manque pour y arriver : le wake word ([veille](../veille/etudes/wake-word.md)), le branchement de jabfy-voice sur jabfy-core, la convergence de la V0.0.1 sur `main`, et le choix de l'intégration entre la voix (Python) et jabfy-tts (Rust).

## Étapes mesurées

Chaque étape a son chronomètre, pour savoir où part le temps. Détail dans [Performance › Latence](../performance/latence.md).

| Étape                              | Composant               | Mesure             | Valeur mesurée (27/10/2026)                |
| ---------------------------------- | ----------------------- | ------------------ | ------------------------------------------ |
| Détection du wake word             | jabfy-voice             | `t_wake`           | Pas encore de wake word                    |
| Fin de parole → texte              | jabfy-voice             | `t_stt`            | À mesurer                                  |
| Demande → proposition              | jabfy-core + modèle     | `t_llm`            | 0,3 à 3,6 s selon le modèle et le matériel |
| Proposition → décision → exécution | jabfy-bus + jabfy-guard | `t_verif + t_exec` | 0,65 ms avec audit sur disque              |
| Texte → premier son                | jabfy-tts               | `t_tts`            | À mesurer                                  |
