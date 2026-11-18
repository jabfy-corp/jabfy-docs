# jabfy-desktop

| Responsable | Code                                                                    | Mise à jour |
| ----------- | ----------------------------------------------------------------------- | ----------- |
| Eloi        | Electron, React, TypeScript ; squelette sur `main` (un écran d'accueil) | 18/11/2026  |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par le responsable.

## Le problème constaté

* **L'utilisateur a besoin d'une interface** pour parler à Jabfy, voir l'état de la maison et l'historique des actions.
* **L'interface ne doit porter aucune décision** : elle affiche et transmet, Core propose, Guard décide.
* **L'équipe est petite** : il faut partager le plus de code possible entre ordinateur, web et mobile.

## Les technologies et pourquoi

| Besoin                | Choix                                                             | Pourquoi                                                                   | Écarté                                                                                                |
| --------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Application de bureau | Electron ([ADR-0004](../architecture/adr/0004-electron-react.md)) | Déjà utilisé dans le prototype ; un seul code pour Windows, macOS et Linux | Tauri : bien plus léger, mais un cœur en Rust à apprendre. Applications natives : trois bases de code |
| Interface             | React et TypeScript                                               | Mêmes composants que le futur client web                                   | —                                                                                                     |
| Construction          | Vite                                                              | Démarrage instantané en développement                                      | —                                                                                                     |

## Ce que la veille change

* **Electron embarque un navigateur Chromium complet** : souvent plus de 100 Mo de mémoire au repos. Si l'application doit tourner sur la box à côté du modèle de langage, cette mémoire manque au modèle. **Tauri 2** (stable depuis octobre 2024) utilise le moteur web du système et produit des applications bien plus légères : à réévaluer avant d'écrire du vrai code, tant que le squelette est vide.
* **Aucun responsable n'est disponible avant la semaine 8** de la roadmap.

## Sources

* [Electron](https://www.electronjs.org/), [Tauri 2](https://v2.tauri.app/)
* [Tauri : présentation et taille des applications](https://v2.tauri.app/start/)
