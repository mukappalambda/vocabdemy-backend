SHELL := /bin/bash

help: ## Show help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Remove __pycache__ and .pytest_cache
	@echo "$(WHALE) $@"
	@find . -type d -name '__pycache__' | xargs -I{} rm -rf {}
	@find ./app -name ".pytest_cache" | xargs rm -rf

install: ## Install project dependencies
	@echo "$(WHALE) $@"
	@uv sync

remove-python-env: ## Remove the virtual environement
	@echo "$(WHALE) $@"
	@uv venv -c

env: ## Create .env
	@echo "$(WHALE) $@"
	@cp .env.example .env

clean-env:
	@echo "$(WHALE) $@"
	@rm -f .env

build: install ## Build the container image
	@echo "$(WHALE) $@"
	@PYTHON_VERSION=$$(cat PYTHON_VERSION); \
	APP_VERSION=$$(poetry run cz version -p); \
	docker build -t vocabdemy:$${APP_VERSION} \
	--build-arg PYTHON_VERSION=$${PYTHON_VERSION} \
	--build-arg APP_VERSION=$${APP_VERSION} .

build-dev: ## Build the dev container image
	@echo "$(WHALE) $@"
	@PYTHON_VERSION=$$(cat PYTHON_VERSION); \
	APP_VERSION=$$(poetry run cz version -p); \
	docker build -t vocabdemy:test -f Dockerfile.dev \
	--build-arg PYTHON_VERSION=$${PYTHON_VERSION} \
	--build-arg APP_VERSION=$${APP_VERSION} .

test: ## Run tests
	@echo "$(WHALE) $@"
	@POSTGRES_DB_URL=sqlite:///demo uv run pytest

update-lockfile: ## Update the project's lockfile
	@echo "$(WHALE) $@"
	@uv lock --frozen

export-requirements: ## Export the lockfile to requirements.txt
	@echo "$(WHALE) $@"
	@uv export --no-dev --no-hashes --no-annotate > requirements.txt

rmi-dangling: ## Remove dangling container images
	@echo "$(WHALE) $@"
	@docker images --filter dangling=true -qa | xargs -I{} docker rmi {}

images-filter: ## List images
	@echo "$(WHALE) $@"
	@docker images --filter reference=vocabdemy

dev: ## Run the container stack for development
	@echo "$(WHALE) $@"
	@docker compose -f docker-compose-dev.yml up

prod: ## Run the container stack for production
	@echo "$(WHALE) $@"
	@docker compose up -d

style: ## Format source code
	@echo "$(WHALE) $@"
	@uv run ruff format ./app
	@uv run ruff check --extend-select I app
