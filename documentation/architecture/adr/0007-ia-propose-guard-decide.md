# 0007 — L'IA propose, une vérification déterministe décide

| Statut                                              | Date       | Auteurs | Veille liée                                   |
| --------------------------------------------------- | ---------- | ------- | --------------------------------------------- |
| Accepté (principe fondateur, consigné a posteriori) | 27/10/2026 | Équipe  | [LLM local](../../veille/etudes/llm-local.md) |

## Contexte

Un modèle de langage peut se tromper, inventer, ou être manipulé par le texte qu'on lui donne (injection de prompt). Or Jabfy pilote des serrures, des alarmes et du chauffage. Les mesures du 27/10/2026 le confirment : Llama 3.2 a proposé d'éteindre une lumière en réponse à « Quelle heure est-il ? » ([Intentions](../../performance/intentions.md)).

## Options étudiées

1. **Le modèle exécute directement** ses décisions (appel d'outil vers l'appareil) — simple, mais toute erreur du modèle devient une action réelle.
2. **Le modèle propose, l'utilisateur confirme chaque action** — sûr, mais pénible au quotidien.
3. **Le modèle propose, une vérification déterministe décide**, et seules les actions à risque demandent une confirmation humaine.

## Décision

Option 3. Le modèle ne produit qu'une **proposition JSON**. Toute commande passe par le Verification Engine du bus, qui délègue la décision à **jabfy-guard** (niveaux de risque, politiques, refus par défaut). Le bus refuse toute exécution qui ne vient pas d'une approbation valide (`VerificationBypass`), et chaque décision est écrite dans un audit infalsifiable **avant** l'exécution. Dans la V0.0.1, l'utilisateur clique en plus sur « Appliquer » pour chaque proposition.

## Conséquences

* Une erreur ou une manipulation du modèle ne peut pas, à elle seule, déclencher une action dangereuse.
* La sécurité repose sur la qualité des règles de Guard : le vérificateur actuel de jabfy-core, qui ne contrôle que les noms d'appareils, ne suffit pas, et doit déléguer à Guard.
* Chaque action est traçable : qui l'a demandée, quelle règle l'a autorisée, ce qui a été exécuté.
