# Installation et lancement

> ⚠️ Page recopiée automatiquement depuis [jabfy-deploy/docs/installation.md](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docs/installation.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Prérequis

- Git et accès aux dépôts Jabfy concernés.
- Docker avec le plugin Compose prenant en charge `up --wait`, et daemon démarré.
- Python 3 pour le lanceur, pas pour les applications qui tournent en conteneurs.
- Ports locaux 8080 et 1883 libres, connexion Internet pour le premier build et
  le téléchargement du modèle, espace disque disponible.

## Sources compatibles

Depuis un dossier parent vide destiné aux clones :

```bash
git clone --branch deploy-1-bootstrap-container-deployment git@github.com:jabfy-corp/jabfy-deploy.git
git clone --branch core-3-publish-container-image git@github.com:jabfy-corp/jabfy-core.git
git clone --branch bus-2-publish-container-image git@github.com:jabfy-corp/jabfy-bus.git
git clone --branch guard-4-v001-deployment git@github.com:jabfy-corp/jabfy-guard.git
git clone --branch sim-2-v001-deployment git@github.com:jabfy-corp/jabfy-simulation.git
cd jabfy-deploy
```

Les cinq dépôts doivent être frères. Si les clones existent déjà, ne pas les
écraser : sauvegarder les modifications locales avant de choisir les branches.
Cette liste décrit la livraison V0.0.1 ; les autres branches de développement
ne sont pas automatiquement compatibles. Le lanceur ne clone ni ne change de branche.

## Démarrer

Toutes les commandes suivantes s'exécutent depuis `jabfy-deploy` :

```bash
python3 scripts/start.py --check
python3 scripts/start.py
```

La première commande vérifie les marqueurs de compatibilité et la syntaxe Compose,
sans démarrer Docker ni tester le runtime. La seconde construit les images, attend
les contrôles de santé, puis demande à Ollama de télécharger `qwen2.5:1.5b`.
Le premier lancement peut prendre plusieurs minutes.

Ouvrir **http://127.0.0.1:8080**. Dans le panneau IA : actualiser les modèles,
sélectionner le modèle, demander une proposition puis cliquer sur Appliquer.
Aucune proposition n'est exécutée automatiquement.

```bash
python3 scripts/start.py --no-ai
```

`--no-ai` évite uniquement le téléchargement : Core et Ollama démarrent quand même.
Les contrôles manuels fonctionnent sans modèle ; un modèle déjà présent reste utilisable.

Pour choisir explicitement le modèle par défaut ou changer les ports :

```bash
python3 scripts/start.py --model qwen2.5:1.5b
SIM_PORT=8082 MQTT_PORT=1884 python3 scripts/start.py --no-ai
```

Dans le second cas, ouvrir http://127.0.0.1:8082. Réutiliser les mêmes variables aux
lancements suivants. Voir [Configuration](interfaces.md) pour leur portée.

## Sans lanceur Python

```bash
docker compose -f compose.local.yml up --build -d --wait --wait-timeout 180
docker compose -f compose.local.yml exec -T ollama ollama pull qwen2.5:1.5b
```

Compose seul ne télécharge aucun modèle. Ne pas remplacer ces commandes par un
simple `docker compose up` : celui-ci sélectionne la configuration GHCR historique.

Pour arrêter sans perdre les données :

```bash
docker compose -f compose.local.yml stop
```

Voir [Exploitation](exploitation.md) pour la relance, les sauvegardes et les erreurs.
