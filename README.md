
## Lancer le serveur

Dans le répertoire `/backend` :

```bash
make build # la première fois, puis à chaque changement dans la construction de l'image docker
make up
```

## Specs de l'api

Lancer le serveur, puis :

- <http://localhost:5000/static/swagger-ui-3.17.6/dist/index.html>

## Configuration

Pour configurer la base de donnée sur une plateforme autre qu'un poste de développeur, vous pouvez renseigner les valeurs suivantes dans un fichier `.env` (non versionné) situé au même endroit que le fichier `application.py`.

Par exemple :

```dotenv
DATABASE_USER = postgres
DATABASE_PASSWORD = example
DATABASE_HOST = database
DATABASE_PORT = 5432
DATABASE_NAME = postgres
```
