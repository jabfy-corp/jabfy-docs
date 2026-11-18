# jabfy-deploy

| Responsable | Code                                                             | Mise à jour |
| ----------- | ---------------------------------------------------------------- | ----------- |
| Loan        | Docker Compose et Python ; V1 en cours sur la branche `deploy-5` | 18/11/2026  |

> Raisons reconstituées à partir du code, des ADR et des mesures. À confirmer par le responsable.

## Le problème constaté

* **Quatre applications, chacune sur sa branche, plus un broker MQTT et un serveur de modèles.** Les lancer à la main demande de connaître chaque repo.
* **« Ça marche chez moi »** : sans versions figées, deux personnes ne lancent pas le même code. Le mentor a demandé de figer les versions du bus et de Guard.
* **Rien ne vérifie qu'un déploiement fonctionne** de bout en bout. Le mentor a demandé une batterie de tests de déploiement en CI/CD.

## Les technologies et pourquoi

| Besoin                    | Choix                                                                                                     | Pourquoi                                                                             | Écarté                                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Emballer chaque composant | Docker : la V1 construit chaque image à partir de son commit figé                                         | Le même environnement sur toutes les machines                                        | Installation Python directe : dépend de la machine                                                                     |
| Assembler la pile         | Docker Compose                                                                                            | Une seule machine (la box de la maison) : Compose suffit et se lit facilement        | Kubernetes, k3s : faits pour plusieurs machines, trop lourds pour une box                                              |
| Figer les versions        | `sources.lock.json` (un commit exact par composant), images Mosquitto et Ollama figées par empreinte      | Un déploiement se rejoue à l'identique ; changer de version, c'est changer une ligne | Branches ou étiquettes `latest` : changent sans prévenir. Sous-modules Git : plus difficiles à manipuler pour l'équipe |
| Piloter                   | Script Python `deploy.py` (`up`, `status`, `logs`, `down`, `model`)                                       | Python est déjà requis par l'équipe ; une commande par geste                         | Makefile : moins portable sous Windows. Ansible : utile pour gérer un parc de machines, pas une seule                  |
| Tester                    | `pytest` qui lance la vraie pile Docker : découverte, commande d'un appareil, persistance, mode restreint | Prouve que les composants fonctionnent ensemble, pas seulement chacun de son côté    | —                                                                                                                      |

## Ce que la veille change

* **Le verrou ne couvre pas tout** : les Dockerfiles téléchargent encore leur image Python et leurs dépendances au moment de la construction. Pour aller plus loin : figer aussi les images de base et les dépendances (fichier de verrouillage par composant).
* **Le test de bout en bout doit tourner en CI** à chaque changement du verrou, pour répondre à la demande du mentor.

## Sources

* [Docker Compose](https://docs.docker.com/compose/), [k3s](https://k3s.io/)
* [Docker : figer une image par son empreinte](https://docs.docker.com/reference/cli/docker/image/pull/)
* Doc du composant : [jabfy-deploy](../composants/jabfy-deploy/)
