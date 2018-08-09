L'application "Il manque du beurre" est une application prétexte pour donner un exemple de comment structurer un code backend qui s'appuie sur une base de donnée.

C'est une API destinée à signaler qu'il manque un produit à la maison. Par exemple, s'il manque du beurre à la maison, je peux faire un `POST` sur le produit manquant `'beurre'` et l'API l'enregistre.

Ensuite, toute personne du foyer peut consulter les produits manquants à acheter en faisant un `GET` sur l'API (voir les specs plus bas).

-----

- [Sujets couverts](#sujets-couverts)
    - [Ce que vous pouvez apprendre en lisant ce code](#ce-que-vous-pouvez-apprendre-en-lisant-ce-code)
- [Démarrer la plateforme](#d-marrer-la-plateforme)
- [Lancer les tests](#lancer-les-tests)
    - [Sélectionner le(s) test(s) à lancer](#s-lectionner-le-s-test-s-lancer)
- [Specs de l'api](#specs-de-l-api)
- [Configuration](#configuration)
- [Migrations de base de données](#migrations-de-base-de-donn-es)
    - [Créer une nouvelle version](#cr-er-une-nouvelle-version)
    - [Supprimer les versions trop anciennes](#supprimer-les-versions-trop-anciennes)
- [TODO](#todo)

## Sujets couverts

Ce dépot permet de démarrer :

- Un backend & une API HTTP (en Python 3)
- Le backend s'appuie sur une base de donnée (PostgreSQL)

### Ce que vous pouvez apprendre en lisant ce code

Ce dépot contient une partie des besoins communs des projets webs qui démarrent auxquels j'ai participé, tout langage & frameworks confondus.

- Structurer le code du backend en [architecture hexagonale][archi-hexa]
- Tester automatiquement un backend en Python 3 (tests unitaires et tests d'intégration)
- Connecter le tout avec des containers Docker et un `Makefile`
- Configurer la connection à la base de donnée par des variables d'environnement
- Gérer les migrations de base de données par des scripts

Note : la plupart des éléments ci-dessus sont transposables dans d'autres langages que Python. Par exemple, le code est très découplé du framework HTTP (ici [Flask][flask]).

[archi-hexa]: https://blog.octo.com/architecture-hexagonale-trois-principes-et-un-exemple-dimplementation/
[flask]: http://flask.pocoo.org/


## Démarrer la plateforme

```bash
make build  # la première fois, puis à chaque changement dans la construction de l'image docker
make database-upgrade  # la première fois, puis à chaque nouvelle version de la base de donnée
make up
```

Pour plus d'infos :

```bash
make help
```

## Lancer les tests

Lancer les tests unitaires :

```bash
make backend-test-unit
```

Lancer les tests d'intégration :

```bash
make backend-test-integration
```

Lancer le linter :

```bash
make backend-lint
```

Lancer le linter et tous les tests :

```bash
make backend-test-all
```

### Sélectionner le(s) test(s) à lancer

Pendant le développement, il est utile de ne lancer qu'un seul test ou une seule suite de tests pour se concentrer sur un comportement (surtout pour les tests non unitaires, plus lents).

Pour faire ça, on peut temporairement annoter le test à lancer avec `@pytest.mark.only` par exemple, puis ajouter les arguments `-m only` à la commande qui exécute les tests.

Les targets de test du `Makefile` permettent de faire ça avec des variables d'environnement.

Par exemple :

```bash
INTEGRATION_TEST_OPTIONS='-m only' make backend-test-integration
```

En général, j'ajoute cette commande comme _Run Configuration_ supplémentaire dans IntelliJ par exemple, en plus des configurations qui lancent tous les tests.

Attention : ne pas commiter les `@pytest.mark.only` qui vous ont servi au développement.

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

## TODO

- Étendre l'API (pouvoir signaler qu'un produit n'est plus manquant)
- Améliorer le bootstrap
- Améliorer la déserialisation des produits connus
- Test end to end ? Acceptance ?
- Utiliser l'ORM SQL Alchemy (côté infra backend uniquement) ?
- Discussion boilerplate passe-plat vs appeler un repo dans le controller
- Discussion & prospositions pour aller plus loin, authent (membres de la famille), gestion des rôles, backoffice (admin)
- Un frontend ? En Cycle.js ?
