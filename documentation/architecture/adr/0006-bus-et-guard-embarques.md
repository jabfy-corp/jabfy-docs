# ADR-0006 — Bus et Guard embarqués comme bibliothèques dans la V0.0.1

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Accepté pour la V0.0.1 (consigné a posteriori) ; à réexaminer | 27/10/2026 | Équipe | — |

## Contexte

Pour la V0.0.1, il fallait une pile locale complète qui se lance en une commande : maison virtuelle, propositions de l'IA, vérification et exécution. jabfy-bus et jabfy-guard sont des bibliothèques Python. La question était de savoir où les faire tourner.

## Options étudiées

1. **Deux services réseau séparés** (un conteneur Bus, un conteneur Guard) — découplage maximal, mais deux API à sécuriser et une latence réseau à chaque commande.
2. **Embarqués dans jabfy-simulation** — un seul processus pour la maison, le bus et Guard ; Guard est branché comme `authorizer` du Verification Engine.
3. **Embarqués dans jabfy-core** — Core propose et exécute dans le même processus (exploré sur la branche `core-12-bus-integration`).

## Décision

Pour la V0.0.1, **bus et Guard sont embarqués dans le runtime de jabfy-simulation**. jabfy-deploy lance quatre conteneurs : simulation, Core, Ollama et Mosquitto. Il n'y a pas de faux service Bus ou Guard.

## Conséquences

- Pas d'API supplémentaire à sécuriser, et une décision de Guard ne coûte qu'un appel de fonction.
- Core ne fait que proposer : l'exécution reste du côté de la maison, ce qui renforce la règle « l'IA propose, Guard autorise, le Bus exécute ».
- **Deux lignes coexistent** : la branche `core-12-bus-integration` embarque le bus dans Core. Il faut choisir la cible avant de fusionner ces branches sur `main` : c'est un point à trancher en équipe.
