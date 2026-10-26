# Sécurité — règles d'or du bus

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/security.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/security.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## 1. Lecture / écriture séparées

- Tout adapter est **read-only par défaut** (`AdapterMode.READ_ONLY`).
- L'écriture est un opt-in explicite à deux niveaux : le mode de
  l'adapter ET, pour Modbus, le `write_allowed` de chaque registre.
- `WriteNotAllowed` est levée sur toute tentative non autorisée.

## 2. Toute commande passe par le Verification Engine

```text
command.requested → Verification Engine → command.approved | command.rejected
                                              ↓
                                       Execution Layer
                                              ↓
                                         Audit append-only
```

Interdit absolu : `IA → publish MQTT direct`. L'Execution Layer lève
`VerificationBypass` si le message n'est pas un `command.approved`, ne
provient pas du Verification Engine, n'a pas de `correlation_id`, ou
(si un `approval_validator` est configuré) n'a pas d'admission valide.

### Admission à usage unique (V0.0.1)

- Le Verification Engine mémorise chaque approbation émise (copie du
  message exact) pendant son dispatch synchrone uniquement.
- `ExecutionLayer(approval_validator=engine.consume_approval)` n'exécute
  que la commande **identique (même `to_dict()`)** à celle approuvée, **une
  seule fois** : un rejeu ou un payload modifié lève `VerificationBypass`.
- `VerificationEngine(authorizer=...)` délègue la décision à un
  autorisateur externe (Guard dans la maison virtuelle) : son résultat
  remplace alors les policies historiques. Si l'autorisateur échoue, la
  commande est **refusée** (`guard_error`, risque `critical`).
- Sans ces options, le mode historique autonome est inchangé.

## 3. Niveaux de risque

| Niveau | Exemple | Validation |
|---|---|---|
| `low` | Lire une température | Auto (default allow) |
| `medium` | Allumer une lumière | Policy explicite requise |
| `high` | Ouvrir une porte, désactiver l'alarme | Policy stricte (default deny) |
| `critical` | Action machine, coupure énergie | Policy stricte + contexte (default deny) |

Le risque est `max(risque de l'action, plancher du domaine cible)` :
une action anodine sur une serrure reste `high`. Une action ou un
domaine inconnus sont classés `critical` (on ne devine jamais qu'une
commande est bénigne).

Les actions de position (`set_position`, `set_tilt`) et de mode
(`set_mode`, traduite en `system_mode` pour Zigbee2MQTT) sont `medium` :
volets et climatisation demandent donc une policy explicite.

## 4. Policies

Déclaratives, évaluées dans l'ordre, première qui matche gagne.
Critères : risque max, domaines, actions, entités, lieux, niveau de
confiance minimal de la source, fenêtre horaire (gère les fenêtres
passant minuit). Sans match : **default deny** au-delà de `low`.

## 5. Niveaux de confiance

`untrusted < local_network < local_gateway < verified_device < internal`

Le `trust_level` est estampillé par l'adapter émetteur et entre dans
l'évaluation des policies (`min_trust`).

## 6. Audit

- Append-only, JSON Lines, un enregistrement par ligne.
- Chaînage SHA-256 : chaque enregistrement embarque le hash du
  précédent ; `jabfy-bus audit-verify <fichier>` détecte toute
  altération.
- Tracés automatiquement : tous les `command.*` + les messages `audit`.
- **Écrit avant dispatch** : si un `audit` est fourni au Verification
  Engine, la décision est journalisée (flush + `fsync`) *avant* la
  publication de l'approbation. Une erreur d'écriture empêche l'envoi.
- Après une erreur d'I/O, le journal se verrouille (`OSError`) tant qu'il
  n'est pas rouvert et vérifié.
- À l'ouverture d'un fichier existant, la chaîne est vérifiée : une chaîne
  corrompue lève `ValueError` et **refuse d'être prolongée**.
  `verify_file()` renvoie `False` au lieu de lever sur un fichier invalide.
- Écritures protégées par un verrou (`RLock`) : sûr entre threads.

## 7. Surfaces d'exposition

- L'API HTTP/WebSocket (`jabfy-bus serve`) est **en lecture seule** :
  aucun endpoint d'exécution. Les commandes entrent uniquement par le
  bus. Ce n'est pas le runtime de la V0.0.1, qui est porté par
  `jabfy-simulation` et orchestré par `jabfy-deploy`.
- Origines autorisées (`api.allowed_origins`, défaut
  `http://localhost:5173`) :
  - HTTP : CORS limité à ces origines, méthode `GET` et en-tête
    `Content-Type` uniquement, sans credentials ;
  - WebSocket : un navigateur envoie toujours `Origin` ; une origine
    absente de la liste est refusée (fermeture 1008). Un client sans
    `Origin` (CLI, service local) reste accepté.
  - `register_ws_routes(app, bus, allowed_origins=...)` applique la
    même règle quand le bus est embarqué dans un autre service (Core).
    Sans liste, toute connexion navigateur est refusée.
- Broker MQTT : TLS + ACL obligatoires en production, jamais d'accès
  anonyme, attention aux retained messages (une vieille commande
  conservée peut être rejouée).
