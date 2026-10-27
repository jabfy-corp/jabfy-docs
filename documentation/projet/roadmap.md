# Roadmap et jalons

Cette page donne la vue d'ensemble des grandes étapes de développement. Chaque jalon validé devient une **milestone GitHub**, et chaque tâche une **issue** rattachée à cette milestone.

## Où en est le projet (27/10/2026)

| Bloc | État |
|---|---|
| Bus JSON universel (jabfy-bus) | ✅ Sur `main` : adapters, vérification, exécution, audit, admission à usage unique, image Docker. 96 tests. |
| Raisonnement (jabfy-core) | ✅ `POST /act` sur `main`, 30 tests ; la version V0.0.1 est sur une branche |
| Autorisation (jabfy-guard) | 🟡 Bibliothèque fonctionnelle, sur la branche V0.0.1, pas encore sur `main` |
| Maison virtuelle 3D (jabfy-simulation) | 🟡 Fonctionnelle dans la V0.0.1, sur une branche |
| Lancement en une commande (jabfy-deploy) | 🟡 Fonctionnel dans la V0.0.1, sur une branche |
| **V0.0.1 : maison virtuelle pilotée par l'IA** | ✅ **Livrée et démontrable**, à partir de branches compatibles |
| Voix (jabfy-voice) | 🟡 Boucle micro → transcription → réponse → voix, pas encore branchée sur Core |
| Synthèse vocale (jabfy-tts) | 🟡 Bibliothèque Rust autour de Kokoro, pas encore utilisée par la voix |
| Clients (desktop, web, mobile) | ⚪ Squelettes, hors du périmètre actuel |
| Documentation | ✅ Site unique, doc de chaque composant synchronisée automatiquement, veille, architecture et premières mesures |

## Grandes étapes

| Phase | Objectif | État |
|---|---|---|
| 0 — Correctifs | CORS corrigés, fournisseur de modèle interchangeable | ✅ Terminée |
| 1 — Base du bus | Messages normalisés, vérification, exécution, audit | ✅ Terminée |
| 2 — V0.0.1 | Maison virtuelle pilotée par l'IA, en local, lancée en une commande | ✅ Livrée sur branches |
| 3 — Convergence | La V0.0.1 sur `main`, CI verte partout, un seul contrat d'API pour Core | 🔵 En cours |
| 4 — Commande vocale | « Jabfy, allume le salon » de bout en bout : wake word, transcription, Core, Guard, Bus, réponse vocale | ⚪ À venir |
| 5 — Matériel réel | Vrais appareils Zigbee via Zigbee2MQTT, sur une machine cible définie | ⚪ À venir |
| 6 — Clients et Matter | Interfaces desktop, web, mobile ; adapter Matter | ⚪ Après l'EIP si besoin |

## Jalons proposés

À valider au RDV du 29/10, puis à créer comme milestones GitHub.

| Jalon | Contenu | Critère de fin | Date cible |
|---|---|---|---|
| J1 — V0.0.1 sur `main` | Fusion des branches V0.0.1 (core, guard, simulation, deploy), choix de l'emplacement du bus, CI de jabfy-simulation réparée | La V0.0.1 se lance depuis cinq clones de `main` | À fixer |
| J2 — Choix des modèles | Mesure du WER (STT) et des intentions (LLM) sur des jeux étendus ; machine cible définie | ADR « modèle par défaut » et « taille du modèle STT » acceptés | À fixer |
| J3 — Commande vocale | Wake word « Jabfy », voix branchée sur Core, réponse par Kokoro | Une commande dite à voix haute allume une lampe de la maison virtuelle | À fixer |
| J4 — Matériel réel | Zigbee2MQTT avec une clé USB et quelques appareils | Le même scénario fonctionne sur de vrais appareils | À fixer |

## Historique

| Date | Étape |
|---|---|
| 07/09/2026 | Client de modèle interchangeable (llama.cpp, Ollama) dans jabfy-core |
| 29/09 – 11/10/2026 | Raisonnement headless, intégration bus ↔ simulation, ligne V0.0.1 |
| 16/10/2026 | RDV de suivi : choix des objectifs EIP (1, 2, A, D) |
| 24/10/2026 | Mise en place du site de documentation |
| 26/10/2026 | V0.0.1 du bus fusionnée sur `main` (PR #6) ; documentation du bus |
| 27/10/2026 | Documentation de core, deploy, simulation, tts et voice ; veille, architecture et premières mesures de performance |
