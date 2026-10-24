# Latence de bout en bout

| Responsable | Valeur de départ | Cible | Dernière mesure |
|---|---|---|---|
| | | | |

## Définition

Temps entre la fin de la phrase de l'utilisateur et le premier son de la réponse, décomposé par étape (voir [Flux d'une demande](../architecture/flux.md)) :

`t_total = t_stt + t_llm + t_verif + t_exec + t_tts`

`t_wake` (détection du mot d'activation) est mesuré à part, car il précède la fin de la phrase.

Tant que la voix n'est pas branchée, on mesure la partie texte : de la demande reçue par Core jusqu'au nouvel état de l'appareil virtuel (`t_llm + t_verif + t_exec`).

## Protocole de mesure

- Scénarios jabfy-simulation à définir (au moins : une commande simple, une commande refusée, une demande hors sujet).
- Horodatage de chaque étape à partir du `correlation_id`, qui suit la demande de bout en bout.
- 30 exécutions par scénario ; médiane et p95.

## Résultats

| Date | Commits | Machine | Modèle | Étape | Médiane | p95 |
|---|---|---|---|---|---|---|
| | | | | | | |

## Optimisations testées

| Date | Optimisation | Avant | Après | Gardée ? |
|---|---|---|---|---|
| | | | | |
