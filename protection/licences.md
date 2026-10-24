# Licences

## Licences des repos

État au 24/10/2026.

| Repo | Visibilité | Licence déclarée |
|---|---|---|
| jabfy-bus | Privé | Propriétaire (`LICENSE` : « All rights reserved ») |
| jabfy-simulation | Privé | Propriétaire (`pyproject.toml`) |
| jabfy-deploy | Privé | Aucune |
| jabfy-website | Privé | Aucune |
| jabfy-tts | Public | MIT dans `package.json`, sans fichier `LICENSE` |
| jabfy-core | Public | Aucune |
| jabfy-guard | Public | Aucune |
| jabfy-voice | Public | Aucune |
| jabfy-desktop | Public | Aucune |
| jabfy-web | Public | Aucune |
| jabfy-mobile | Public | Aucune |
| jabfy-prototype | Public | Aucune |
| jabfy-template | Public | Aucune |

Un repo public sans licence reste « tous droits réservés » : on peut le lire, mais personne n'a légalement le droit de le réutiliser. Ce n'est ni de l'open source, ni une protection explicite.

### Décisions à prendre

- [ ] Choisir une politique commune : quels repos sont open source, sous quelle licence, et lesquels restent propriétaires.
- [ ] Vérifier la cohérence : jabfy-core est public mais dépend de jabfy-bus, privé et propriétaire.
- [ ] Ajouter un fichier `LICENSE` dans chaque repo, et dans jabfy-template pour les futurs repos.
- [ ] Consigner la politique dans un ADR.

## Licences des dépendances et des modèles

La licence d'un modèle (ses poids) est souvent différente de celle du code qui le fait tourner, et certains modèles de TTS ou de wake word sont réservés à un usage non commercial. À vérifier sur la page officielle de chaque modèle, version par version.

| Élément | Utilisé dans | Licence du code | Licence du modèle | Usage commercial | Vérifié le |
|---|---|---|---|---|---|
| Kokoro-82M | jabfy-tts | | | | |
| faster-whisper | jabfy-voice | | | | |
| pyttsx3 | jabfy-voice | | | | |
| Ollama | jabfy-deploy, jabfy-voice | | sans objet | | |
| qwen2.5:1.5b | jabfy-deploy | sans objet | | | |
| llama3.2 | jabfy-voice | sans objet | | | |
| paho-mqtt, fastapi, pymodbus, pyyaml | jabfy-bus (extras) | | sans objet | | |
| Pydantic | jabfy-guard | | sans objet | | |

Pour les dépendances de code, un outil peut produire l'inventaire : `pip-licenses` côté Python, `license-checker` côté npm.
