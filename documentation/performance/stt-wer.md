# Taux d'erreur du STT (WER)

| Suivi par | Valeur de départ | Cible | Dernière mesure |
|---|---|---|---|
| Elias | À mesurer (faster-whisper `base`) | Proposée : WER < 10 % sur les commandes | — |

## Définition

*Word Error Rate* : (substitutions + suppressions + insertions) / nombre de mots de la référence, sur un jeu de phrases en français. Plus c'est bas, mieux c'est.

## Protocole de mesure

- Jeu de phrases de commandes domotiques en français, avec leur transcription de référence, versionné dans le repo (à créer).
- Enregistrements par plusieurs voix, au calme et avec bruit de fond.
- Normalisation identique des deux côtés avant comparaison (casse, ponctuation, nombres).
- Calcul avec une bibliothèque standard, par exemple `jiwer`.

## Résultats

| Date | Moteur et modèle | Jeu de phrases | Condition | WER | Temps de transcription |
|---|---|---|---|---|---|
| | | | | | |

## Optimisations testées

| Date | Optimisation | Avant | Après | Gardée ? |
|---|---|---|---|---|
| | | | | |
