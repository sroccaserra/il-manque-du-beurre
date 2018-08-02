###############################################################################
#
#  More Makefile hints here:
#  - <http://clarkgrubb.com/makefile-style-guide>
#

END_TO_END_TEST_OPTIONS ?=
# END_TO_END_TEST_PATH = /app/test/end_to_end
INTEGRATION_TEST_OPTIONS ?=
INTEGRATION_TEST_PATH = /app/test/integration
UNIT_TEST_OPTIONS ?=
UNIT_TEST_PATH = /app/test/unit
COVERAGE_REPORT ?= xml:coverage.xml

###############################################################################
# Prerequisites

.PHONY: build
build:
	docker build ./ -t il_manque_du_beurre_backend

###############################################################################
# Start and stop the whole platform

.PHONY: up
up:
	docker-compose up -d backend
	scripts/wait_for_services.sh localhost 5000

.PHONY: down
down:
	docker-compose down


###############################################################################
# General housekeeping

.PHONY: clean
clean: clean-docker clean-python

.PHONY: clean-docker
clean-docker:
	docker container rm -f $(shell docker container ps -aq)
	docker image rm $(shell docker images --quiet --filter "dangling=true")

.PHONY: clean-python
clean-python:
	find . | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf


###############################################################################
# Lint and test

.PHONY: lint
lint:
	docker run --rm -v $(shell pwd):/app il_manque_du_beurre_backend \
		flake8 --config=/app/setup.cfg /app *.py

.PHONY: test-unit
test-unit:
	docker run --rm -v $(shell pwd):/app il_manque_du_beurre_backend \
		pytest -vvv --color=yes $(UNIT_TEST_OPTIONS) $(UNIT_TEST_PATH)

.PHONY: test-integration
test-integration:
	docker run --rm -v $(shell pwd):/app il_manque_du_beurre_backend \
		pytest -vvv --color=yes $(INTEGRATION_TEST_OPTIONS) $(INTEGRATION_TEST_PATH)

.PHONY: test-end-to-end
test-end-to-end: up
	docker-compose exec -T backend \
		pytest -vvv --color=yes $(END_TO_END_TEST_OPTIONS) $(END_TO_END_TEST_PATH)

.PHONY: test-all
test-all: lint up
	docker-compose exec -T backend \
		pytest \
		--color=yes \
		--junitxml=junit.xml \
		--cov-report $(COVERAGE_REPORT) \
		--cov-report term-missing:skip-covered \
		--cov=/app/sheldon_trends/domain \
		--cov=/app/sheldon_trends/infrastructure \
		$(UNIT_TEST_PATH) \
		$(INTEGRATION_TEST_PATH) \
		$(END_TO_END_TEST_PATH)

###############################################################################
# More detailed run targets

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: bash
bash: up
	docker-compose exec backend bash
