# Équipe

Qui travaille sur quoi : c'est la première page à consulter pour savoir à qui poser une question sur un repo.

| Personne | GitHub                                       | Repos principaux                                                  | Rôle |
| -------- | -------------------------------------------- | ----------------------------------------------------------------- | ---- |
| Elias    | [@Elious84](https://github.com/Elious84)     | jabfy-bus, jabfy-voice, jabfy-docs                                |      |
| Eloi     | [@katu-dev](https://github.com/katu-dev)     | jabfy-tts, jabfy-desktop, jabfy-web, jabfy-mobile, jabfy-template |      |
| Joan     | [@joanartepi](https://github.com/joanartepi) | jabfy-core                                                        |      |
| Loan     | [@GnXloan](https://github.com/GnXloan)       | jabfy-deploy, jabfy-guard, jabfy-simulation, jabfy-website        |      |
| Simeon   | [@Lycoris69](https://github.com/Lycoris69)   | jabfy-prototype, jabfy-core                                       |      |

## Responsables par repo

D'après l'historique Git : à confirmer par chacun.

| Repo             | Responsable | Relecteur |
| ---------------- | ----------- | --------- |
| jabfy-core       | Loan        | Siméon    |
| jabfy-bus        | Elias       | Joan      |
| jabfy-guard      | Loan        | Joan      |
| jabfy-simulation | Loan        | Siméon    |
| jabfy-deploy     | Loan        |           |
| jabfy-voice      | Elias       |           |
| jabfy-tts        | Eloi        |           |
| jabfy-desktop    | Eloi        |           |
| jabfy-web        | Eloi        |           |
| jabfy-mobile     | Eloi        |           |
| jabfy-website    | Loan        |           |
| jabfy-docs       | Elias       |           |

## Documentation des composants

État au 27/10/2026, d'après l'historique Git.

| Composant                                                       | Rédigée par                   | Date  | Sur le site                                |
| --------------------------------------------------------------- | ----------------------------- | ----- | ------------------------------------------ |
| jabfy-bus                                                       | Elias, carte du code par Joan | 26/10 | ✅                                          |
| jabfy-core                                                      | Simeon                        | 27/10 | ✅                                          |
| jabfy-simulation                                                | Simeon                        | 27/10 | ✅                                          |
| jabfy-deploy                                                    | Loan                          | 27/10 | ✅                                          |
| jabfy-tts                                                       | Eloi                          | 27/10 | ✅                                          |
| jabfy-voice                                                     | Elias                         | 27/10 | En attente de fusion (PR)                  |
| jabfy-guard, desktop, web, mobile, website, prototype, template | —                             | —     | Pas encore de code à documenter sur `main` |

## Répartition des pages

> Proposition, à valider au prochain RDV. Chacun remplit ses pages par PR et peut échanger avec un autre membre : il suffit de mettre ce tableau à jour.

En plus de ces pages, chaque responsable tient à jour le `docs/` de ses repos (voir [Écrire la doc d'un repo](../contribuer/ecrire-la-doc.md)).

| Personne | Veille                                                                                             | Architecture et ADR                                                                                                                                         | Performance                                                                      | Protection                                                                                             |
| -------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Elias    | [Protocoles domotiques](../veille/etudes/protocoles-domotiques.md), [STT](../veille/etudes/stt.md) | [Interfaces](../architecture/interfaces.md)                                                                                                                 | [WER](../performance/stt-wer.md), [Bus](../performance/bus.md)                   |                                                                                                        |
| Eloi     | [TTS](../veille/etudes/tts.md)                                                                     | [ADR-0004 Electron/React](../architecture/adr/0004-electron-react.md)                                                                                       |                                                                                  | [Licences](../protection/licences.md), [Marque et antériorité](../protection/marque-et-anteriorite.md) |
| Joan     | [LLM local](../veille/etudes/llm-local.md)                                                         | [Flux](../architecture/flux.md), [ADR-0002 FastAPI](../architecture/adr/0002-fastapi.md), [ADR-0003 Modèle local](../architecture/adr/0003-modele-local.md) | [Intentions](../performance/intentions.md)                                       |                                                                                                        |
| Loan     |                                                                                                    | [Vue globale](../architecture/vue-globale.md), [CI/CD](../architecture/ci-cd.md)                                                                            | [Latence](../performance/latence.md), [CPU et RAM](../performance/ressources.md) | [Sécurité des repos](../protection/securite.md)                                                        |
| Simeon   | [Wake word](../veille/etudes/wake-word.md), [Vie privée](../veille/etudes/vie-privee.md)           |                                                                                                                                                             | [Wake word](../performance/wake-word.md)                                         | [RGPD](../protection/rgpd.md), [Propriété intellectuelle](../protection/propriete-intellectuelle.md)   |
