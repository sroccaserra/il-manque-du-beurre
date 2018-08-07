###############################################################################
#
#  More Makefile hints here:
#  - <http://clarkgrubb.com/makefile-style-guide>
#

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c

END_TO_END_TEST_OPTIONS ?=
INTEGRATION_TEST_OPTIONS ?=
UNIT_TEST_OPTIONS ?=
COVERAGE_REPORT ?= xml:coverage.xml


# https://www.client9.com/self-documenting-makefiles/
.PHONY: help
help:  ## Prints this help
	@awk -F ':|##' '/^[^\t].+?:.*?##/ { \
	printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
	}' $(MAKEFILE_LIST)


###############################################################################
# Prerequisites

.PHONY: build
build:  ## builds the platform's docker images (prerequisite, do it once & when changing images)
	docker build --tag=il_manque_du_beurre_backend backend/
	docker build --tag=il_manque_du_beurre_database database/

###############################################################################
# Database

.PHONY: database-start
database-start:  ## Starts the database and waits for it (timeouts after 60 seconds)
	docker-compose up -d database
	docker-compose exec -T database \
		bash scripts/wait_for_services.sh database 5432

.PHONY: database-init
database-init: database-start  ## Creates the databases (needed for integration tests & above)
	docker-compose exec -T database \
		bash scripts/create_databases.sh


###############################################################################
# Start and stop the whole platform

.PHONY: up
up: database-start  ## Starts the whole platform
	docker-compose up -d backend

.PHONY: down
down:  ## Stops the whole platform
	docker-compose down



###############################################################################
# General housekeeping

.PHONY: clean
clean: clean-docker clean-backend  ## Cleans docker & python stuff

.PHONY: clean-docker
clean-docker:  ## Removes dangling docker containers & images
	docker container rm -f $(shell docker container ps -aq)
	docker image rm $(shell docker images --quiet --filter "dangling=true")

.PHONY: clean-backend
clean-backend:  ## Removes Python build files
	find backend | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf


###############################################################################
# Lint and test

.PHONY: lint
lint:  ## Lints the backend code
	docker-compose exec -T backend \
		flake8 --config=setup.cfg . *.py

.PHONY: test-unit
test-unit:  ## Runs the backend unit tests
	docker-compose exec -T backend \
		pytest -vvv --color=yes $(UNIT_TEST_OPTIONS) test/unit

.PHONY: test-integration
test-integration: database-start  ## Runs the backend integration tests
	docker-compose exec -T backend \
		pytest -vvv --color=yes $(INTEGRATION_TEST_OPTIONS) test/integration

.PHONY: test-all
test-all: lint database-start  ## Lints & runs all the backend tests with coverage
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


###############################################################################
# More detailed run targets

.PHONY: logs
logs:  ## Follows the logs of the whole platform
	docker-compose logs -f

.PHONY: logs-backend
logs-backend:  ## Follows the backend logs
	docker-compose logs -f backend

.PHONY: logs-database
logs-database:  ## Follows the database logs
	docker-compose logs -f database

.PHONY: bash-backend
bash-backend:  ## Starts a bash session on the running backend
	docker-compose exec backend bash

.PHONY: bash-database
bash-database:  ## Starts a bash session on the running database
	docker-compose exec database bash
