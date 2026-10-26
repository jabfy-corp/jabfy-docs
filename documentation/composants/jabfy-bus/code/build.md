# jabfy-bus — build, Docker et CI

> ⚠️ Page recopiée automatiquement depuis [jabfy-bus/docs/code/build.md](https://github.com/jabfy-corp/jabfy-bus/blob/main/docs/code/build.md). Toute modification faite ici sera écrasée : modifiez le repo d'origine.

| fichier | ce qu'il fait |
|---|---|
| `pyproject.toml` | Python ≥ 3.10 ; extras `mqtt`, `api`, `modbus`, `yaml`, `all` ; commande `jabfy-bus`. |
| `Dockerfile`, `.dockerignore` | Image du bus en service autonome (`jabfy-bus serve`). |
| `Makefile` | Raccourcis : `test` (unittest), `demo`, `lint` (ruff), `install`, `dev`. |
| `schemas/bus-message-1.0.json` | Schéma JSON publié de l'enveloppe `BusMessage`. |
| `examples/config.example.yaml` | Exemple de config du bus. |
| `.github/workflows/ci.yml` | Matrice Python 3.10 / 3.11 / 3.12. |
| `.github/workflows/pr-validation.yml`, `publish-image.yml` | Validation de PR, publication d'image. |
