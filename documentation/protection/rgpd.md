# RGPD

Le fonctionnement 100 % local est un vrai argument : si aucune donnée ne quitte la maison, Jabfy ne transmet rien à un tiers. Encore faut-il le démontrer et documenter ce qui est conservé sur place.

## Inventaire des données

| Donnée                                 | Collectée par                | Stockée où          | Durée de conservation | Quitte la maison ? |
| -------------------------------------- | ---------------------------- | ------------------- | --------------------- | ------------------ |
| Audio du micro                         | jabfy-voice                  |                     |                       | Non (à démontrer)  |
| Transcriptions                         | jabfy-voice, jabfy-core      |                     |                       |                    |
| Demandes et propositions du modèle     | jabfy-core                   |                     |                       |                    |
| Journal d'audit des commandes          | jabfy-bus                    | Fichier append-only |                       |                    |
| États et télémétrie des appareils      | jabfy-bus                    |                     |                       |                    |
| Inventaire des appareils et des pièces | jabfy-core, jabfy-simulation |                     |                       |                    |

## À démontrer

* [ ] Aucun trafic sortant pendant un scénario complet, hors téléchargement initial des modèles : capture réseau à joindre ici.
* [ ] Pas de télémétrie dans les dépendances (serveur de modèles, bibliothèques), ou télémétrie désactivée.

## À documenter pour l'utilisateur

* Ce qui est enregistré, où, et combien de temps.
* Comment consulter et effacer ses données.
* Ce qui change si un jour une fonction en ligne est ajoutée.

Voir aussi la fiche de veille [Vie privée](../veille/etudes/vie-privee.md).
