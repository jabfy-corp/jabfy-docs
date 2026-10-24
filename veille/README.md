# Méthode de veille

> Objectif obligatoire 1 : *Track what's out there and use it to crack your project's hard problem.*

Chaque problème dur a sa page, et toutes suivent le même [modèle](modele.md). Une veille aboutit toujours à une décision : le choix retenu est consigné dans un [ADR](../architecture/adr/README.md), qui renvoie vers la fiche de veille.

## Critères fixes

Toutes les fiches comparent les solutions sur les mêmes critères, pour pouvoir les mettre côte à côte :

| Critère | Ce qu'on note |
|---|---|
| 100 % local | Fonctionne sans aucun appel réseau sortant, une fois installé |
| Latence | Mesurée sur la machine cible, protocole décrit dans [Performance](../performance/README.md) |
| Qualité en français | Score mesuré (WER, MOS, taux de compréhension…) ou appréciation argumentée |
| RAM | Empreinte mémoire en fonctionnement |
| Licence | Licence du code **et** licence des modèles, qui sont souvent différentes |

Une fiche peut ajouter des critères propres à son domaine (par exemple la sécurité native pour les protocoles), mais ne retire jamais les critères fixes.

## Fiches

| Domaine | Fiche | Statut |
|---|---|---|
| Détection du mot d'activation | [Wake word](wake-word.md) | À faire |
| Reconnaissance vocale | [STT](stt.md) | À faire |
| Modèle de langage local | [LLM local](llm-local.md) | À faire |
| Synthèse vocale | [TTS](tts.md) | À faire |
| Protocoles domotiques | [Protocoles domotiques](protocoles-domotiques.md) | Audit existant à reprendre |
| Vie privée | [Vie privée](vie-privee.md) | À faire |

## Bonnes pratiques

- Dater chaque mesure et noter la version testée : un tableau de veille vieillit vite.
- Citer ses sources avec un lien.
- Préférer une mesure faite par nous, sur la machine cible, à un chiffre annoncé par l'éditeur.
- Vérifier la licence des **poids** du modèle : certains modèles de TTS ou de wake word sont réservés à un usage non commercial.
