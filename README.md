L'application "Il manque du beurre" est une application prétexte pour donner un exemple de comment structurer un code backend qui s'appuie sur une base de donnée.

C'est une API destinée à signaler qu'il manque un produit à la maison. Par exemple, s'il manque du beurre à la maison, je peux faire un `POST` sur le produit manquant `'beurre'` et l'API l'enregistre.

Ensuite, toute personne du foyer peut consulter les produits manquants à acheter en faisant un `GET` sur l'API (voir les specs plus bas).

## Sujets couverts

Ce dépot contient ce qu'il faut pour démarrer :

- Un backend & une API HTTP en Python 3
- Le backend s'appuie sur une base de donnée PostgreSQL

Ce que vous pouvez apprendre en lisant ce code :

- Structurer le code du backend en [architecture hexagonale][archi-hexa]
- Tester automatiquement un backend en Python 3 (tests unitaires et tests d'intégration)
- Connecter le tout avec des containers Docker et un `Makefile`
- Configurer la connection à la base de donnée par des variables d'environnement
- Gérer les migrations de base de données par des scripts

La plupart des éléments ci-dessus sont applicables dans d'autres langages que Python. Par exemple, le code est très découplé du framework HTTP (ici [Flask][flask]).

[archi-hexa]: https://blog.octo.com/architecture-hexagonale-trois-principes-et-un-exemple-dimplementation/
[flask]: http://flask.pocoo.org/


## Démarrer la plateforme

```bash
make build  # la première fois, puis à chaque changement dans la construction de l'image docker
make database-start database-upgrade  # la première fois, puis à chaque nouvelle version de la base de donnée
make up
```

Pour plus d'infos :

```bash
make help
```

## Specs de l'api

Lancer la plateforme, puis :

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
DATABASE_NAME = ilmanquedubeurre
```

## Migrations de base de données

Le projet utilise [Alembic][alembic] pour gérer les migrations de base de données.

Pour appliquer toutes les migrations de base de données disponibles :

```bash
make database-upgrade
```

Pour appliquer ces migrations sur la base de donnée de tests :

```bash
ALEMBIC_NAMESPACE=test_database make database-upgrade
```

Note : la variable d'environnement `ALEMBIC_NAMESPACE` permet d'appliquer les tâches de migration à la base applicative (par défaut), ou à la base de tests (`ALEMBIC_NAMESPACE=test_database`).

Les autres opérations de migration de base de données fonctionnent sur le même modèle.

Voir le `Makefile`, ou `make help` pour les autres opérations.

[alembic]: http://alembic.zzzcomputing.com

### Créer une nouvelle version

Pour créer un script de migration vers une nouvelle version :

```bash
REVISION_MESSAGE='Création de la table des produits manquants' make database-revision
```

Note : pas besoin de namespace ici, les scripts de version servent pour la base applicative et pour la base de test.

Ensuite, éditer le nouveau fichier qui a été généré dans `database/alembic/versions`.

### Supprimer les versions trop anciennes

S'il y a trop de versions, il est possible de générer un script reflétant l'état actuel, voir :

- http://alembic.zzzcomputing.com/en/latest/cookbook.html#building-an-up-to-date-database-from-scratch

Ensuite, ce script devrait pouvoir être placé dans `/docker-entrypoint-initdb.d`, où il sera lancé à la création du container de la base de donnée (voir un exemple dans le `Dockerfile` de la base de donnée). Ne pas oublier la base de donnée de tests.

Les versions trop anciennes peuvent ensuite être supprimées.
