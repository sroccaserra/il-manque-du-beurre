
## Démarrer la plateforme

```bash
make build  # la première fois, puis à chaque changement dans la construction de l'image docker
make up
```

Pour plus d'infos :

```bash
make help
```

## Specs de l'api

Lancer le serveur, puis :

- <http://localhost:5000/static/swagger-ui-3.17.6/dist/index.html>

Note : c'est un Swagger minimaliste d'essai.

## Configuration

Pour configurer la base de donnée sur une plateforme autre qu'un poste de développeur, vous pouvez définir les variables suivantes dans l'environnement du backend ou les renseigner dans un fichier `.env` (non versionné) situé au même endroit que le fichier `application.py`.

Par exemple :

```dotenv
DATABASE_USER = postgres
DATABASE_PASSWORD = example
DATABASE_HOST = database
DATABASE_PORT = 5432
DATABASE_NAME = postgres
```

## Sujets couverts

Ce dépot contient ce qu'il faut pour démarrer :

- Un backend & une API HTTP en Python 3
- Le backend s'appuie sur une base de donnée PostgreSQL

Ce que vous pouvez apprendre en lisant ce code :

- Strucuturer le code du backend en [architecture hexagonale][archi-hexa]
- Tester automatiquement un backend en Python 3 (tests unitaires et tests d'intégration)
- Connecter le tout avec des containers et un `Makefile`
- Configurer la connection à la base de donnée par des variables d'environnement
- Gérer les migrations de base de données par des scripts

[archi-hexa]: https://blog.octo.com/architecture-hexagonale-trois-principes-et-un-exemple-dimplementation/
