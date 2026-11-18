# jabfy-core : comprendre la demande et proposer une action

| Responsables | Code | Mise à jour |
|---|---|---|
| Loan, Siméon | Python 3.11 ; `main`, intégration du bus sur la branche `core-12` | 18/11/2026 |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par les responsables.

## Le problème constaté

- **Un modèle de langage n'est pas fiable.** Lors de nos mesures, un modèle de 3 milliards de paramètres a éteint une lumière en réponse à « Quelle heure est-il ? » ([Intentions](../../performance/intentions.md)). Le JSON renvoyé peut aussi être mal formé ou citer un appareil qui n'existe pas.
- **Le modèle et la machine ne sont pas encore choisis.** Il faut pouvoir en changer sans réécrire Core.
- **Tout doit tourner sur la machine de l'utilisateur**, sans appel au cloud.

## Les technologies et pourquoi

| Besoin | Choix | Pourquoi | Écarté |
|---|---|---|---|
| Faire tourner le modèle | Ollama (llama.cpp en option) | Installation en une commande, modèles quantifiés pour CPU, API compatible OpenAI | vLLM : pensé pour les GPU de serveur. API cloud : contraire au 100 % local |
| Parler au modèle | Un seul client compatible OpenAI, derrière l'interface `LLMClient` ([ADR-0003](../../architecture/adr/0003-modele-local.md)) | Changer de moteur ou de modèle ne demande que de la configuration | Une classe par fournisseur : du code à chaque ajout. API native d'Ollama : lie Core à un seul moteur |
| Orchestration de l'IA | Code maison avec `httpx` | Le flux est court (une demande, une proposition) : un framework ajouterait des couches à comprendre et à déboguer. `httpx` permet de simuler le serveur dans les tests | LangChain, LlamaIndex : lourds, API qui change souvent, utiles surtout pour le RAG et les agents complexes |
| API HTTP | FastAPI ([ADR-0002](../../architecture/adr/0002-fastapi.md)) | Validation des entrées et documentation OpenAPI générées depuis les modèles Pydantic | Flask : validation à écrire à la main |
| Valider la réponse du modèle | Pydantic, `jsonschema` (branche `core-12`), puis jabfy-guard | Le modèle propose, une vérification déterministe décide ([ADR-0007](../../architecture/adr/0007-ia-propose-guard-decide.md)) | Faire confiance au modèle : démenti par nos mesures |

## Ce que la veille change

- **Sorties structurées.** Ollama et llama.cpp peuvent imposer un schéma JSON à la génération. Le JSON est alors toujours valide et ne cite que des appareils connus. Cela ne rend pas la compréhension meilleure ([LLM local](../llm-local.md)).
- **Le vérificateur actuel ne suffit pas.** Il ne contrôle que les noms d'appareils et les booléens : l'action non demandée de la mesure serait passée. D'où la priorité donnée à jabfy-guard.
- **Direction du 17/11 : un orchestrateur et des spécialistes.** Core appelle la voix, la synthèse et plus tard la vision comme des outils, avec un point d'accès au modèle par rôle. À surveiller : l'appel d'outils natif des moteurs locaux, et le [Model Context Protocol](https://modelcontextprotocol.io/) comme format standard pour décrire ces outils.
- **Trois versions de l'API coexistent** (`/act`, `/simulation/propose`, `/prompt`). Le contrat cible reste à choisir.

## Sources

- [Ollama : sorties structurées](https://ollama.com/blog/structured-outputs)
- [llama.cpp : serveur compatible OpenAI](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
- [HTTPX : transports pour les tests](https://www.python-httpx.org/advanced/transports/)
- Étude détaillée : [LLM local](../llm-local.md)
