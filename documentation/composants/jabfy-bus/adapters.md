# Guide des adapters

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/adapters.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/adapters.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

## Contrat commun (`adapters/base.py`)

Un adapter :

1. hérite de `BaseAdapter` et déclare son `protocol` ;
2. traduit les données natives en `BusMessage` via `emit()` (qui
   estampille adapter, protocole et trust_level) ;
3. conserve TOUJOURS le payload natif dans `raw` et l'adresse native
   dans `source.raw_address` ;
4. publie sa santé via `report_health()` ;
5. est read-only sauf configuration explicite.

Les clients réseau (MQTT, Modbus, HTTP) sont **injectables** : le
code de normalisation se teste sans réseau ni matériel.

## MQTT (`adapters/mqtt`) — P0

- `TopicMapper` : règles déclaratives `pattern → domaine/classe/unité`,
  wildcards `+` et `#`.
- Les topics sans règle sont comptés (`dropped`) et ignorés : on ne
  devine pas la sémantique d'un topic inconnu.
- Écriture : `write(topic, payload)` publie en QoS 1, jamais retained.

## HTTP (`adapters/http`) — P0

- `HTTPPollingAdapter` : liste d'`Endpoint` avec extraction par chemin
  pointé (`value_path="relay.power"`). Un endpoint HS ne bloque pas
  les autres.
- `WebhookReceiver` : routes par préfixe, normaliseur dédié par route,
  la logique est testable sans serveur (`handle_payload`).

## Zigbee2MQTT (`adapters/zigbee2mqtt`) — P0

- Jamais de Zigbee brut : on consomme les topics `zigbee2mqtt/#`.
- Un payload multi-exposes produit **un message par expose**
  (temperature, humidity, battery…), chacun portant le payload complet.
- `contact` est inversé à la normalisation (true = fermé → door=false).
- L'inventaire `bridge/devices` enrichit les messages (modèle,
  fabricant, adresse IEEE).

## Modbus TCP (`adapters/modbus`) — P1

- Un registre sans sémantique est inutilisable : le `RegisterMap`
  attache entité, classe, unité, échelle et politique d'écriture.
- Triple contrôle en écriture : mode adapter + `write_allowed` du
  registre + type de registre réellement inscriptible.

## CoAP (`adapters/coap`) — P2

Squelette : le contrat de normalisation est fixé
(`handle_response`), le transport (aiocoap/DTLS) viendra plus tard.

## À venir

| Adapter | Priorité | Voie d'intégration |
|---|---|---|
| Matter | P1 | librairie existante (python-matter-server) |
| OPC UA | P1/P2 | read + subscribe minimal |
| Z-Wave | P2 | via Z-Wave JS (MQTT/WebSocket) |
| BACnet | P2 | BACpypes |
| KNX | P2/P3 | passerelle IP |
| BLE | P2/P3 | scan présence + capteurs |
| LoRaWAN | P3 | application server (TTN/ChirpStack) |
