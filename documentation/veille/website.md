# jabfy-website

| Responsable | Code                                                                             | Mise à jour |
| ----------- | -------------------------------------------------------------------------------- | ----------- |
| Loan        | React, Vite, Tailwind ; serveur Express ; premier commit sur `main` (30/04/2026) | 18/11/2026  |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par le responsable.

## Le problème constaté

* **Présenter Jabfy** au public et aux jurys : ce que fait le produit et pourquoi le 100 % local compte.
* **Recueillir des contacts** : formulaire de contact et inscription à la lettre d'information.

## Les technologies et pourquoi

| Besoin    | Choix                                                                                        | Pourquoi                                                                  | Écarté                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Pages     | React, Vite, Tailwind CSS, framer-motion                                                     | Même pile que les clients : l'équipe la connaît déjà ; animations simples | Générateur de site statique (Astro, Hugo) : plus léger pour un site sans application, mais une pile de plus |
| Serveur   | Node.js, Express, `zod` pour valider les formulaires, `helmet` pour les en-têtes de sécurité | Recevoir les formulaires de contact et de lettre d'information            | Service de formulaires hébergé : les données partent chez un tiers                                          |
| Lancement | Docker Compose                                                                               | Même outil que jabfy-deploy                                               | —                                                                                                           |

## Ce que la veille change

* **Toutes les dépendances sont en version `latest`** : deux constructions à un jour d'écart peuvent donner deux sites différents, ou ne plus compiler. Figer les versions (`package-lock.json`).
* **Les formulaires ne stockent rien** pour l'instant. Dès qu'ils enregistreront des adresses e-mail, le RGPD s'applique : consentement explicite, droit de suppression ([RGPD](../protection/rgpd.md)).
* **Le serveur ne sert qu'aux formulaires** : un site statique avec un formulaire hébergé en Europe suffirait peut-être. À trancher selon ce que le site doit faire.

## Sources

* [Astro](https://astro.build/), [Vite](https://vite.dev/)
* [npm : rôle de package-lock.json](https://docs.npmjs.com/cli/configuring-npm/package-lock-json)
* [CNIL : formulaires et prospection](https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique)
