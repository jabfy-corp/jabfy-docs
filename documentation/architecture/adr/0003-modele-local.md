# ADR-0003 — Modèle local via une API compatible OpenAI

| Statut | Date | Auteurs | Veille liée |
|---|---|---|---|
| Proposé (rétroactif) | | | [LLM local](../../veille/llm-local.md) |

> Décision déjà appliquée, consignée après coup. Contexte et options à compléter par l'équipe avant de passer en « Accepté ».

## Contexte

Le raisonnement doit tourner entièrement en local. Le prototype et jabfy-voice appelaient Ollama directement. Le plan initial de jabfy-core prévoyait une classe par fournisseur de modèles.

## Options étudiées

1. **Une classe par fournisseur** (Ollama, llama.cpp…) — chaque backend est exploité au mieux, mais chaque ajout demande du code.
2. **Un client unique pour l'API compatible OpenAI** derrière une interface `LLMClient` — Ollama et `llama-server` (llama.cpp) exposent tous deux cette API, donc changer de serveur ne demande que de la configuration.
3. **Appel direct à l'API native d'Ollama** — simple, mais lie Core à un seul serveur.

## Décision

Option 2 : jabfy-core passe par l'interface `LLMClient` et un client unique compatible OpenAI. jabfy-deploy fournit Ollama avec `qwen2.5:1.5b` par défaut.

## Conséquences

- Le serveur de modèles et le modèle se choisissent par configuration, sans toucher au code de Core.
- Les fonctions propres à un serveur, hors de l'API commune, ne sont pas accessibles.
- jabfy-voice appelle encore Ollama directement : à aligner quand la voix sera rebranchée sur Core.
