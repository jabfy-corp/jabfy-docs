# Débit et latence du bus

| Suivi par | Valeur de départ      | Cible                                              | Dernière mesure |
| --------- | --------------------- | -------------------------------------------------- | --------------- |
| Elias     | Mesurée le 27/10/2026 | < 10 ms par commande, mémoire stable dans le temps | 27/10/2026      |

## Définition

* **Débit** : nombre de messages de télémétrie par seconde que le bus publie et distribue à ses abonnés.
* **Latence d'une commande** : temps entre la publication d'un `command.requested` et la fin de son traitement complet : classification du risque, décision, écriture de l'audit, admission, traduction MQTT et publication du `command.executed`.
* **Mémoire retenue** : mémoire qui reste allouée après le passage des messages.

## Protocole de mesure

* Script : [`benchmarks/bench_bus.py`](https://github.com/jabfy-corp/jabfy-docs/blob/main/benchmarks/bench_bus.py), sur le code de `main` de jabfy-bus.
* **Débit** : 20 000 messages de télémétrie, 5 répétitions, médiane. Le registre d'entités et un abonné universel sont branchés, comme dans un bus réel.
* **Latence** : 2 000 commandes avec un audit en mémoire, puis 500 avec un audit sur disque et `fsync`, comme dans la V0.0.1. Le transport MQTT est remplacé par une fonction vide : on mesure le bus, pas le réseau.
* **Mémoire** : `tracemalloc` après 100 000 messages.

## Résultats

| Date       | Commit jabfy-bus | Machine                           | Mesure                                                | Résultat                                     |
| ---------- | ---------------- | --------------------------------- | ----------------------------------------------------- | -------------------------------------------- |
| 27/10/2026 | `c99d086`        | i7-13700HX, SSD NVMe, Python 3.12 | Débit, publication seule                              | **\~550 000 messages/s**                     |
| 27/10/2026 | `c99d086`        | idem                              | Débit, création et validation des messages comprises  | \~100 000 messages/s                         |
| 27/10/2026 | `c99d086`        | idem                              | Latence d'une commande, audit en mémoire              | **médiane 0,10 ms**, p95 0,12 ms             |
| 27/10/2026 | `c99d086`        | idem                              | Latence d'une commande, audit sur disque avec `fsync` | **médiane 0,65 ms**, p95 0,98 ms             |
| 27/10/2026 | `c99d086`        | idem                              | Mémoire retenue                                       | **\~124 octets par message, jamais libérés** |

Résultats bruts : [`benchmarks/resultats/`](../../benchmarks/resultats/).

## Analyse

* **Le bus n'est pas le goulot d'étranglement** : une commande complète, avec un audit écrit sur disque, coûte moins d'une milliseconde, quand le modèle de langage met de 0,3 à 3,5 s ([Intentions](intentions.md)).
* **L'écriture de l'audit sur disque multiplie la latence par 6** (`fsync` à chaque décision). C'est le prix voulu de la garantie « l'audit est écrit avant l'exécution », et il reste négligeable.
* **Fuite de mémoire** : pour ignorer les doublons, le bus garde l'identifiant de chaque message reçu, sans jamais le purger. À un message par seconde, cela représente environ 10 Mo par jour, soit près de 4 Go par an pour un bus qui tourne en continu.

## Optimisations à tester

| Date    | Optimisation                                                                                        | Avant                                 | Après          | Gardée ? |
| ------- | --------------------------------------------------------------------------------------------------- | ------------------------------------- | -------------- | -------- |
| À faire | Limiter la déduplication à une fenêtre (par exemple les 10 000 derniers identifiants, ou une durée) | \~124 octets par message, sans limite | Mémoire bornée | —        |
