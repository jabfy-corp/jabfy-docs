# Tableau de bord et méthode

> Objectif complémentaire D : _Measure, test and optimize technical performance._

Chaque métrique a sa page, construite sur le même [modèle](modele.md) : définition, protocole de mesure, valeur de départ, cible, résultats, optimisations testées. Les scripts de mesure sont dans [`benchmarks/`](../../../benchmarks/) et peuvent être relancés par n'importe qui.

## Tableau de bord

| Métrique                         | Page                           | Dernière mesure        | Résultat                                                                                                      | Cible                                |
| -------------------------------- | ------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| Compréhension des intentions     | [Intentions](../intentions.md) | 27/10/2026             | **8/10** (Llama 3.2 3B), **10/10** (Ministral 3 8B)                                                           | 10/10, puis ≥ 95 % sur un jeu étendu |
| Débit et latence du bus          | [Bus](../bus.md)               | 27/10/2026             | **0,65 ms** par commande avec audit sur disque ; \~550 000 messages/s ; **fuite de \~124 octets par message** | < 10 ms ; mémoire stable             |
| Latence de bout en bout          | [Latence](../latence.md)       | 27/10/2026 (partielle) | Partie texte : 0,3 à 3,6 s, presque entièrement dans le modèle                                                | < 3 s sur la machine cible           |
| CPU et RAM                       | [Ressources](../ressources.md) | —                      | Modèles : 2 à 6 Go ; machine cible à définir                                                                  | À fixer avec la machine cible        |
| Taux d'erreur du STT (WER)       | [WER](../stt-wer.md)           | —                      | Protocole défini, jeu de phrases à constituer                                                                 | À fixer après la mesure de départ    |
| Faux déclenchements du wake word | [Wake word](../wake-word.md)   | —                      | Bloqué : pas encore de wake word                                                                              | < 1 par jour                         |

## Ce que les premières mesures montrent

1. **Le temps de réponse est presque entièrement celui du modèle de langage** : moins d'une milliseconde pour le bus, de 0,3 à 3,5 s pour le modèle.
2. **La taille du modèle fait la compréhension** : Ministral 3 8B comprend les 10 consignes, Llama 3.2 3B se trompe sur une intention implicite et agit sur une question hors sujet.
3. **Le vérificateur ne peut pas se reposer sur le modèle** : une action non demandée mais syntaxiquement valide passe le vérificateur actuel de jabfy-core. D'où l'intégration de jabfy-guard.
4. **Le bus a une fuite de mémoire** sur la déduplication des messages, à corriger avant de le faire tourner en continu.

## Règles de mesure

* **Reproductible** : chaque mesure indique le commit de chaque repo, la machine, le modèle et sa version. Les scénarios complets passeront par [jabfy-simulation](https://github.com/jabfy-corp/jabfy-simulation), pour pouvoir les rejouer à l'identique et les lancer en CI.
* **Une seule variable à la fois** : une optimisation ne compte que si elle est mesurée avant et après, toutes choses égales par ailleurs.
* **Médiane et p95** plutôt que moyenne pour les latences.
* **Toujours préciser la machine** : une mesure sur une machine de développement avec GPU ne dit rien de la box cible.

## Machines

|     | Machine de mesure actuelle         | Machine cible                                 |
| --- | ---------------------------------- | --------------------------------------------- |
| CPU | Intel Core i7-13700HX (24 threads) | À définir : mini-PC domestique sans GPU dédié |
| RAM | 23 Go                              | À définir (8 à 16 Go visés)                   |
| GPU | NVIDIA RTX 5060 Laptop, 8 Go       | Aucun, a priori                               |
| OS  | Linux 7.0                          | Linux                                         |

Les mesures « CPU seul » de la page [Intentions](../intentions.md) donnent une première idée du comportement sans GPU.
