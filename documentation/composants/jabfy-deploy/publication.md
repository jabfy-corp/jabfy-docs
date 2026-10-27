# Publication des images et de la documentation

> ⚠️ Page recopiée automatiquement depuis [jabfy-deploy/docs/publication.md](https://github.com/jabfy-corp/jabfy-deploy/blob/main/docs/publication.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Images : chemin historique à finaliser

`docker-compose.yml` utilise les images de Core, Bus, Voice et du site vitrine.
Il ne représente pas la maison virtuelle de `compose.local.yml`. Ollama y est
externe ; Voice est facultatif via le profil `voice`.

`deployment.env` contient encore cinq digests `REPLACE_WITH_…`. Ce fichier n'est
pas utilisable tel quel pour un déploiement. Même avec des digests réels, cette
configuration doit être revalidée : notamment, elle configure Core avec
`OLLAMA_HOST`, alors que le Core utilisé par la V0.0.1 attend `JABFY_LLM_BASE_URL`.
Ne pas présenter ce chemin comme une release prête pour la production.

Le workflow `update-image-digest.yml` accepte un événement `image-published` ou un
lancement manuel. Il sélectionne l'image, exige un SHA-256 de 64 caractères
hexadécimaux minuscules, met à jour `deployment.env` et propose une PR.
Il ne lance pas les conteneurs et ne fusionne pas la PR.

| Secret | Emplacement | Rôle |
|---|---|---|
| `JABFY_DEPLOY_DISPATCH_TOKEN` | Repos producteurs | Autoriser la notification à Deploy |
| `JABFY_DEPLOY_PR_TOKEN` | Deploy | Création des PR si le jeton GitHub standard ne suffit pas |

La PR générée nécessite encore une issue réelle et une branche conforme avant
intégration : le workflow actuel utilise l'identifiant du run pour la branche
et ne renseigne pas `Closes #N`. La CI accepte les placeholders de digests comme
valeurs transitoires ; sa réussite ne garantit donc pas un déploiement GHCR fonctionnel.

## Documentation : source unique dans docs/

La convention de `jabfy-docs` est reprise ici : pages en français, un sujet par
page, titre H1, liens relatifs internes et diagrammes Mermaid. Modifier ces sources,
jamais une copie générée dans le dépôt central.

`jabfy-deploy` figure déjà dans `jabfy-docs/composants.txt`. Après fusion du code
et de ces pages sur `main`, le circuit est :

1. Un push modifiant `docs/` déclenche `notify-docs.yml`.
2. Le workflow envoie `docs-updated` à `jabfy-docs`.
3. Le dépôt central clone les sources, recopie les pages, ajoute les liens vers
   leurs sources et régénère la section Composants de son `SUMMARY.md`.
4. GitBook synchronise le dossier `documentation/` du dépôt central.

Le contenu de `documentation/` éventuellement présent dans Deploy via un ancien
export GitBook n'est pas la source de ce mécanisme : il lit exclusivement `docs/`.

## Accès nécessaires

- `DOCS_DISPATCH_TOKEN` dans Deploy : jeton ayant le droit d'envoyer un événement
  au dépôt `jabfy-docs` (Contents: write selon la convention existante).
- `DOCS_SYNC_TOKEN` dans `jabfy-docs` : lecture des dépôts privés listés.

Ne jamais écrire les valeurs de ces secrets dans les pages ou dans Git.
Le workflow central peut aussi être lancé manuellement et tourne chaque nuit.
Un échec de notification n'efface pas les pages déjà publiées.

Les pages de cette branche ne sont pas publiées automatiquement tant qu'elles
ne sont pas sur la branche source synchronisée. Le dossier central généré porte
un marqueur `.synchro`. Les fichiers et dossiers dont le nom commence par `_` ou
`.` sont exclus ; réserver `docs/_interne/` aux notes qui ne doivent pas être publiées.
