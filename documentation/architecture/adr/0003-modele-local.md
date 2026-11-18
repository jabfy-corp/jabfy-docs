# 0003 — Modèle local via une API compatible OpenAI

| Statut                          | Date       | Auteurs | Veille liée                                   |
| ------------------------------- | ---------- | ------- | --------------------------------------------- |
| Accepté (consigné a posteriori) | 27/10/2026 | Équipe  | [LLM local](../../veille/etudes/llm-local.md) |

## Contexte

Le raisonnement doit tourner entièrement en local. Le prototype et jabfy-voice appelaient Ollama directement, avec son API propre. Le premier plan de jabfy-core prévoyait une classe par fournisseur de modèles. Or le choix du modèle et du moteur n'est pas stabilisé : la veille montre qu'il faudra comparer plusieurs modèles, et la machine cible n'est pas encore choisie.

## Options étudiées

1. **Une classe par fournisseur** (Ollama, llama.cpp…) — chaque moteur exploité au mieux, mais chaque ajout demande du code.
2. **Un client unique pour l'API compatible OpenAI**, derrière une interface `LLMClient` — Ollama et le serveur de llama.cpp exposent tous deux cette API : changer de moteur ou de modèle ne demande que de la configuration.
3. **L'API native d'Ollama** — simple, mais lie Core à un seul moteur.

## Décision

Option 2 : jabfy-core passe par l'interface `LLMClient` et un client unique compatible OpenAI. jabfy-deploy fournit Ollama avec `qwen2.5:1.5b` par défaut.

## Conséquences

* Moteur et modèle se choisissent par configuration, sans toucher au code de Core : c'est ce qui a permis de comparer Llama 3.2 et Ministral 3 avec le même code ([Intentions](../../performance/intentions.md)).
* Les fonctions propres à un moteur, hors de l'API commune, ne sont pas accessibles. Les sorties structurées par schéma JSON, recommandées par la veille, passent par le champ `response_format` de l'API compatible.
* jabfy-voice appelle encore Ollama directement : à aligner quand la voix sera branchée sur Core.
