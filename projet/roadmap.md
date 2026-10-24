# Roadmap et jalons

Chaque jalon est une **milestone GitHub**, et chaque tâche une **issue** rattachée à cette milestone. Tout est regroupé dans le GitHub Project de l'organisation. Cette page donne la vue d'ensemble ; l'état détaillé fait foi dans le Project.

## Livraisons

| Version | Contenu | État |
|---|---|---|
| V0.0.1 | Maison virtuelle locale : Simulation (avec Bus et Guard embarqués), Core, Ollama et MQTT lancés par jabfy-deploy | En cours |

## Phases

État relevé le 11/10/2026.

| Phase | Objectif | État |
|---|---|---|
| 0 — Correctifs immédiats | CORS corrigés partout, fournisseur de LLM interchangeable | Terminée, sauf CORS du bus (PR jabfy-bus#6) |
| 1 — Paquet jabfy-guard | Mode forteresse, limitation de débit, confirmation des actions critiques | Exclue le 30/09 ; la bibliothèque Guard est toutefois intégrée à la V0.0.1 |
| 2 — Intégration Core ↔ bus | Événement → bus → Core (LLM) → bus → vérification → exécution → audit | En revue |
| 3 — Maison simulée | Maison factice parlant de vrais protocoles, boucle de retour complète | Partielle |
| 4 — Clients | Bureau, web, mobile | Hors périmètre |
| 5 — Voix | Voix branchée sur Core | Hors périmètre |

## Jalons

| Jalon (milestone) | Date cible | Contenu | Lien |
|---|---|---|---|
| | | | |
