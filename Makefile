.SILENT: all


.PHONY: all
all: lint-check test

.PHONY: env
env:
	python3 -m venv .env --prompt $(shell basename $(shell pwd))

.PHONY: env-delete
env-delete:
	rm -rf .env

.PHONY: env-update
env-update:
	bash -c "source .env/bin/activate && pip install -r requirements.txt && pip install -e ."
	echo "Please don't forget to activate the environment with '.env/bin/activate'!"

# The targets below require the environment to be configured and activated

.PHONY: lint
lint:
	black stonks test setup.py
	isort stonks test setup.py

.PHONY: lint-check
lint-check:
	black --check stonks test setup.py
	isort --check-only stonks test setup.py

.PHONY: test
test:
	pytest test
