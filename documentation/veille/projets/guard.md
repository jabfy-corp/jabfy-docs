# jabfy-guard : décider si une commande est autorisée

| Responsables | Code | Mise à jour |
|---|---|---|
| Loan, Joan | Python 3.11 ; bibliothèque sur la branche `guard-4`, pas encore sur `main` | 18/11/2026 |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par les responsables.

## Le problème constaté

- **Le modèle peut proposer une action que personne n'a demandée** : c'est arrivé lors de nos mesures ([Intentions](../../performance/intentions.md)).
- **Une consigne peut être piégée** (injection de prompt) : un texte lu par le modèle peut le pousser à ouvrir une porte ou désarmer une alarme.
- **Toutes les actions n'ont pas le même risque** : allumer une lampe n'est pas déverrouiller la porte d'entrée.

## Les technologies et pourquoi

| Besoin | Choix | Pourquoi | Écarté |
|---|---|---|---|
| Décider | Règles déterministes en Python, refus par défaut ([ADR-0007](../../architecture/adr/0007-ia-propose-guard-decide.md)) | Même entrée, même décision : testable, explicable. Un niveau de risque par action et par type d'appareil, des bornes sur les paramètres, des limites de fréquence | Voir le comparatif ci-dessous |
| Décrire les données | Pydantic, seule dépendance | Valide la commande et le contexte avant toute règle ; aucun serveur, réseau ou modèle nécessaire | — |
| Brancher Guard | Bibliothèque appelée par le bus (`authorizer`) | Pas de service de plus, pas d'appel réseau sur le chemin critique ([ADR-0006](../../architecture/adr/0006-bus-et-guard-embarques.md)) | Service séparé : latence et une panne de plus |

**Les solutions existantes :**

| Solution | Principe | Pour Jabfy |
|---|---|---|
| Règles maison (choix actuel) | Code Python, catalogue de risques, politiques en JSON | Simple, sans dépendance. Il faut écrire et tester nous-mêmes chaque règle |
| [Open Policy Agent](https://www.openpolicyagent.org/) | Moteur de politiques standard, langage Rego | Éprouvé, mais un service en Go et un langage de plus |
| [Cedar](https://www.cedarpolicy.com/) | Langage de permissions d'AWS, vérifiable formellement | Rigoureux, mais écrit en Rust, sans bibliothèque Python officielle |
| [Casbin](https://casbin.org/) | Bibliothèque de contrôle d'accès par rôles ou attributs, existe en Python | Bon pour « qui peut faire quoi », pas pour les bornes de paramètres et les limites de fréquence |
| Modèle de modération ([Llama Guard](https://github.com/meta-llama/PurpleLlama)), règles de conversation ([NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)) | Un modèle juge le texte | Filtre les contenus, mais sa décision est probabiliste : il peut se tromper ou être trompé |

## Ce que la veille change

- **Deux approches à comparer, à la demande du mentor** : les règles déterministes maintenant, un modèle fine-tuné en Tek5. Le modèle ne pourra que s'ajouter aux règles (refuser plus), jamais les contourner.
- **Guard est le point le plus en retard** : la bibliothèque n'est toujours pas sur `main`, alors que c'est elle qui rend l'IA sûre.

## Sources

- [OWASP Top 10 pour les applications LLM : injection de prompt, actions excessives](https://genai.owasp.org/llm-top-10/)
- Les liens du tableau ci-dessus
