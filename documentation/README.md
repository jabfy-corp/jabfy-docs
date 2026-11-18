# Accueil

Jabfy est un assistant domestique **100 % local** : il comprend une demande, propose une action, la fait vérifier de façon déterministe, puis l'exécute sur les appareils de la maison. Aucune donnée ne quitte le réseau local, et chaque décision est tracée.

Ce site rassemble la documentation transverse de l'EIP : vision, veille, architecture globale, objectifs et comptes-rendus de suivi. La documentation technique de chaque composant vit dans son repo et est recopiée automatiquement dans [Composants](composants/composants.md).

## Où en est le projet

* **La V0.0.1 tourne** : une maison virtuelle 3D, pilotée par une IA locale, lancée en une commande. L'IA propose, Guard autorise, le Bus exécute, et tout est tracé.
* **Prochaine étape** : fusionner la V0.0.1 sur `main`, puis brancher la commande vocale de bout en bout ([Roadmap](projet/roadmap.md)).
* **Premières mesures** : le bus traite une commande en moins d'une milliseconde ; la compréhension dépend fortement de la taille du modèle ([Performance](performance/performance/)).

## Lire en un quart d'heure

Pour préparer un suivi, dans cet ordre :

1. [Compte-rendu préparé du prochain RDV](suivi/2026-10-29.md) : l'avancement et les points à trancher.
2. [Veille, synthèse](veille/veille/) : les six problèmes durs et les choix retenus.
3. [Architecture, en bref](architecture/architecture.md), puis la [vue globale](architecture/vue-globale.md).
4. [Performance, tableau de bord](performance/performance/) et [compréhension des intentions](performance/intentions.md).
5. [Protection, tableau de bord](protection/protection.md).

## Schéma global

```mermaid
flowchart LR
  U([Utilisateur]) -->|voix ou texte| C[Clients<br/>desktop · web · mobile · voice]
  C --> CORE[jabfy-core<br/>raisonnement]
  CORE <-->|API compatible OpenAI| LLM[(Modèle local<br/>Ollama / llama.cpp)]
  CORE -->|proposition d'action| BUS[jabfy-bus<br/>bus JSON · exécution · audit]
  BUS <-->|autorisation| G[jabfy-guard]
  BUS --> D[Appareils<br/>MQTT · Zigbee · Modbus · HTTP]
  SIM[jabfy-simulation<br/>maison virtuelle] -. remplace .-> D
```

L'IA propose, Guard autorise, le Bus exécute. Le détail est dans [Architecture](architecture/architecture.md).

## Repos

| Repo                                                               | Rôle                                                                        | Visibilité |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------- | ---------- |
| [jabfy-core](https://github.com/jabfy-corp/jabfy-core)             | Moteur d'orchestration : API FastAPI, propositions du modèle, validation    | Public     |
| [jabfy-bus](https://github.com/jabfy-corp/jabfy-bus)               | Bus JSON universel : adapters de protocoles, vérification, exécution, audit | Privé      |
| [jabfy-guard](https://github.com/jabfy-corp/jabfy-guard)           | Bibliothèque d'autorisation déterministe des commandes                      | Public     |
| [jabfy-simulation](https://github.com/jabfy-corp/jabfy-simulation) | Maison virtuelle 3D parlant MQTT au format Zigbee2MQTT                      | Privé      |
| [jabfy-deploy](https://github.com/jabfy-corp/jabfy-deploy)         | Assemblage, démarrage et topologie de la stack                              | Privé      |
| [jabfy-voice](https://github.com/jabfy-corp/jabfy-voice)           | Micro, STT, réponse du modèle, synthèse vocale                              | Public     |
| [jabfy-tts](https://github.com/jabfy-corp/jabfy-tts)               | Bibliothèque Rust de synthèse vocale (Kokoro-82M)                           | Public     |
| [jabfy-desktop](https://github.com/jabfy-corp/jabfy-desktop)       | Client Electron + React                                                     | Public     |
| [jabfy-web](https://github.com/jabfy-corp/jabfy-web)               | Client web React                                                            | Public     |
| [jabfy-mobile](https://github.com/jabfy-corp/jabfy-mobile)         | Client React Native / Expo                                                  | Public     |
| [jabfy-website](https://github.com/jabfy-corp/jabfy-website)       | Site vitrine                                                                | Privé      |
| [jabfy-prototype](https://github.com/jabfy-corp/jabfy-prototype)   | Premier prototype Electron + FastAPI + Ollama                               | Public     |
| [jabfy-template](https://github.com/jabfy-corp/jabfy-template)     | Squelette de tout nouveau repo                                              | Public     |

## Où trouver quoi

| Section                                      | Contenu                                                          |
| -------------------------------------------- | ---------------------------------------------------------------- |
| [Projet](projet/projet.md)                   | Vision, équipe, roadmap et jalons                                |
| [Veille](veille/veille/)                     | Objectif obligatoire 1 : une page par problème dur               |
| [Architecture](architecture/architecture.md) | Objectif obligatoire 2 : C4, flux, interfaces, CI/CD, ADR        |
| [Composants](composants/composants.md)       | Doc technique recopiée depuis chaque repo                        |
| [Protection](protection/protection.md)       | Objectif complémentaire A : licences, marque, PI, sécurité, RGPD |
| [Performance](performance/performance/)      | Objectif complémentaire D : métriques et benchmarks              |
| [Contribuer](contribuer/contribuer.md)       | Conventions Git et écriture de la doc                            |
| [Suivi](suivi/suivi/)                        | Comptes-rendus des RDV de suivi                                  |

> Une page de [Composants](composants/composants.md) se modifie **dans son repo d'origine**, jamais dans GitBook : la synchronisation suivante écraserait la modification.
