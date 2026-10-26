# Tests

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/tests.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/tests.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Lancer les tests

```bash
make test
# ou
python3 -m unittest discover -s tests -v
```

96 tests, en moins d'une seconde, sans réseau ni matériel. Sans FastAPI, les 5 tests d'API sont sautés : installer l'extra `api` pour les lancer (`pip install ".[api]"`).

## Ce qui est couvert

| Fichier | Tests | Ce qui est vérifié |
|---|---|---|
| `test_message.py` | 12 | Validation du message v1.0 (type, adapter, action, confiance, `trust_level`), aller-retour JSON, conservation de la valeur brute, `user_situation` |
| `test_bus.py` | 9 | Motifs d'abonnement, déduplication par `message_id`, isolation d'un abonné en erreur, historique |
| `test_verification.py` | 15 | Classification du risque (action et domaine), fenêtres horaires y compris après minuit, policies allow/deny, refus par défaut, niveau de confiance, `correlation_id` |
| `test_admission.py` | 7 | Admission à usage unique, fausse approbation, payload modifié, panne de l'audit ou de l'`authorizer`, journal corrompu |
| `test_execution.py` | 9 | Traduction MQTT et HTTP, protocole ou transport inconnu, audit de l'exécution, contournement de la vérification |
| `test_audit.py` | 7 | Chaînage des hash, détection d'une falsification en mémoire et sur fichier, reprise d'un journal |
| `test_mqtt_adapter.py` | 11 | Jokers `+` et `#`, décodage des payloads, topics non mappés ignorés, écriture refusée en lecture seule |
| `test_zigbee2mqtt.py` | 6 | Un message par expose, inversion de `contact`, payload brut conservé, inventaire du bridge |
| `test_modbus.py` | 9 | Échelle des registres, double opt-in pour l'écriture, registre en panne qui ne bloque pas les autres |
| `test_simulation.py` | 6 | Appareils simulés et pipeline complet en simulation |
| `test_api.py` | 5 | CORS et origines WebSocket (nécessite FastAPI) |

## CI

Le workflow `.github/workflows/ci.yml` tourne à chaque pull request vers `main` et à chaque push sur `main` :

1. les tests, sur Python 3.10, 3.11 et 3.12 ;
2. la démo `jabfy-bus demo --steps 10`, qui échoue si la lampe ne s'allume pas.

La CI n'installe aucun extra : les tests d'API y sont donc sautés. C'est dans les [TODO](README.md).

## Écrire un test

- `unittest` de la bibliothèque standard, un fichier par module testé.
- Les clients réseau (MQTT, Modbus, HTTP) sont injectables : un faux client suffit, comme dans `test_mqtt_adapter.py`.
- Une nouvelle action ou un nouveau type de message demande un test de validation et un test de traduction.
- Une règle de sécurité demande aussi le test du cas refusé, pas seulement du cas accepté.
