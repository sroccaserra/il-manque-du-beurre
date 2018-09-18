##
# Use these environment variables to pass options to pytest.
# Example : `INTEGRATION_TEST_OPTIONS='-m only' make backend-test-integration`
END_TO_END_TEST_OPTIONS ?=
INTEGRATION_TEST_OPTIONS ?=
UNIT_TEST_OPTIONS ?=
COVERAGE_REPORT ?= xml:coverage.xml

##
# Use this environment variable to migrate the test database.
# Example : `ALEMBIC_NAMESPACE='test_database' make database-upgrade`
ALEMBIC_NAMESPACE ?= alembic
ALEMBIC = alembic -n $(ALEMBIC_NAMESPACE)

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c

##
# https://www.client9.com/self-documenting-makefiles/
.PHONY: help
help:  ## Prints this help
	@awk -F ':|##' '/^[^\t].+?:.*?##/ { \
	printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
	}' $(MAKEFILE_LIST)


###############################################################################
# Database

.PHONY: database-start
database-start:  ## Starts the database and waits for it (timeouts after 60 seconds)
	docker-compose up -d database
	docker-compose exec -T database \
		bash scripts/wait_for_services.sh database 5432

.PHONY: database-init
database-init: database-start  ## Inits & migrates both app database & test database to head version
	docker-compose exec -T database \
		alembic -n alembic upgrade head
	docker-compose exec -T database \
		alembic -n test_database upgrade head

.PHONY: database-bash
database-bash:  ## Starts a bash session on the running database container
	docker-compose exec database bash

.PHONY: database-psql
database-psql:  ## Starts a psql session on the running app database
	docker-compose exec database psql --user=postgres --dbname=ilmanquedubeurre

.PHONY: database-psql-test
database-psql-test:  ## Starts a psql session on the running test database
	docker-compose exec database psql --user=postgres --dbname=ilmanquedubeurre_test

.PHONY: database-logs
database-logs:  ## Follows the database logs
	docker-compose logs -f database

.PHONY: database-lint
database-lint:  ## Lints the database code
	docker-compose exec -T database \
		flake8 --config=setup.cfg . *.py

.PHONY: database-current
database-current: database-start  ## Montre la version actuelle de la base de données
	docker-compose exec database $(ALEMBIC) current

.PHONY: database-history
database-history: database-start  ## Montre les versions disponibles de la base de donnée
	docker-compose exec database $(ALEMBIC) history

.PHONY: database-revision
database-revision: database-start  ## Crée une nouvelle version (script de migration) pour la base de donnée
	if [ -z "$(REVISION_MESSAGE)" ]; then echo 'REVISION_MESSAGE not defined'; false; fi
	docker-compose exec database $(ALEMBIC) revision -m "$(REVISION_MESSAGE)"

.PHONY: database-upgrade
database-upgrade: database-start  ## Migre la base de donnée à la version la plus récente
	docker-compose exec -T database $(ALEMBIC) upgrade head

.PHONY: database-downgrade
database-downgrade: database-start  ## Remet la base de donnée à la version précédente (n - 1)
	docker-compose exec database $(ALEMBIC) downgrade -1


###############################################################################
# Backend operations

.PHONY: backend-lint
backend-lint:  ## Lints the backend code
	docker-compose exec -T backend \
		flake8 --config=setup.cfg . *.py

.PHONY: backend-test-unit
backend-test-unit:  ## Runs the backend unit tests
	docker-compose exec -T backend \
		pytest -vvv --color=yes $(UNIT_TEST_OPTIONS) test/unit

.PHONY: backend-test-integration
backend-test-integration: start  ## Runs the backend integration tests
	docker-compose exec -T backend \
		pytest -vvv --color=yes $(INTEGRATION_TEST_OPTIONS) test/integration

.PHONY: backend-test-all
backend-test-all: backend-lint database-start  ## Lints & runs all the backend tests with coverage
	docker-compose exec -T backend \
		pytest \
		--color=yes \
		--junitxml=junit.xml \
		--cov-report $(COVERAGE_REPORT) \
		--cov-report term-missing:skip-covered \
		--cov=il_manque_du_beurre/application \
		--cov=il_manque_du_beurre/domaine \
		--cov=il_manque_du_beurre/infrastructure \
		test/unit \
		test/integration

.PHONY: backend-logs
backend-logs:  ## Follows the backend logs
	docker-compose logs -f backend

.PHONY: backend-bash
backend-bash:  ## Starts a bash session on the running backend container
	docker-compose exec backend bash

.PHONY: backend-clean
backend-clean:  ## Removes Python build files
	find backend | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf


###############################################################################
# Frontend

.PHONY: frontend
frontend:
	cd frontend && npx elm make src/Main.elm --output=dist/index.html


.PHONY: frontend-start
frontend-start:
	cd frontend && npx elm reactor

###############################################################################
# Whole platform management

.PHONY: start
start: database-start  ## Starts the whole platform
	docker-compose up -d backend

.PHONY: stop
stop:  ## Stops the whole platform
	docker-compose down

.PHONY: logs
logs:  ## Follows the logs of the whole platform
	docker-compose logs -f


###############################################################################
# General housekeeping

.PHONY: clean-docker
clean-docker:  ## Removes dangling docker containers & images
	docker container rm -f $(shell docker container ps -aq)
	docker image rm $(shell docker images --quiet --filter "dangling=true")

.PHONY: clean
clean: clean-docker backend-clean  ## Cleans docker & python stuff
