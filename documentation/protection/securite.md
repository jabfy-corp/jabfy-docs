# Sécurité des repos

## État constaté au 27/10/2026

- L'organisation `jabfy-corp` est sur le plan **GitHub Free**.
- La double authentification n'est **pas** obligatoire pour les membres.
- Dependabot et le secret scanning ne sont **pas** activés par défaut sur les nouveaux repos.
- Sur jabfy-core (public), le secret scanning, la protection contre les pushs de secrets et les mises à jour de sécurité Dependabot sont désactivés.

## Mesures à activer

| Mesure | Où | Disponible sur le plan Free | Fait |
|---|---|---|---|
| Double authentification obligatoire | Paramètres de l'organisation | Oui | ☐ |
| Dependabot (alertes et mises à jour de sécurité) | Chaque repo, ou par défaut pour les nouveaux | Oui | ☐ |
| Secret scanning et protection des pushs | Repos publics | Oui | ☐ |
| Secret scanning sur les repos privés | Repos privés | Non : nécessite une offre payante | |
| Protection de la branche `main` (PR obligatoire, CI verte) | Repos publics | Oui | ☐ |
| Protection de branche sur les repos privés | Repos privés | Non : nécessite le plan Team | |

Disponibilités à revérifier dans la doc GitHub si le plan change.

## Règles d'équipe

- Aucun secret dans un repo : utiliser `.env` (ignoré par Git) et un `.env.example` sans valeurs réelles.
- Les tokens des workflows sont des secrets d'organisation, avec les droits minimaux : voir [CI/CD](../architecture/ci-cd.md).
- Un secret poussé par erreur est **révoqué** immédiatement ; le retirer de l'historique ne suffit pas.
- Les failles connues se documentent dans `docs/_interne/`, jamais dans la partie publiée.
