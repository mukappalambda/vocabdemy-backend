SHELL := /bin/bash

.PHONY: clean
clean:
	@find ./app -name "__pycache__" | xargs rm -rf
	@find ./app -name ".pytest_cache" | xargs rm -rf

.PHONY: install
install:
	@poetry install

.PHONY: remove-poetry-env
remove-poetry-env:
	@poetry env remove $$(poetry env list | awk '{print $$1}')

.PHONY: env
env:
	@cp .env.example .env

.PHONY: clean-env
clean-env:
	@rm -f .env

.PHONY: build
build:
	@PYTHON_VERSION=$$(cat PYTHON_VERSION); \
	APP_VERSION=$$(poetry run cz version -p); \
	docker build -t vocabdemy:$${APP_VERSION} \
	--build-arg PYTHON_VERSION=$${PYTHON_VERSION} \
	--build-arg APP_VERSION=$${APP_VERSION} .

.PHONY: build-dev
build-dev:
	@PYTHON_VERSION=$$(cat PYTHON_VERSION); \
	APP_VERSION=$$(poetry run cz version -p); \
	docker build -t vocabdemy:test -f Dockerfile.dev \
	--build-arg PYTHON_VERSION=$${PYTHON_VERSION} \
	--build-arg APP_VERSION=$${APP_VERSION} .

.PHONY: test
test:
	@pushd ./app; \
	POSTGRES_DB_URL=sqlite:///demo poetry run pytest; \
	popd

.PHONY: poetry-lock
poetry-lock:
	@poetry lock --no-update

.PHONY: poetry-export
poetry-export:
	@poetry export -o requirements.txt --without-hashes --without=dev

.PHONY: rmi-dangling
rmi-dangling:
	@docker images --filter dangling=true -qa | xargs -I{} docker rmi {}

.PHONY: images-filter
images-filter:
	docker images --filter reference=vocabdemy

.PHONY: dev
dev:
	@docker compose -f docker-compose-dev.yml up

.PHONY: prod
prod:
	@docker compose up -d

.PHONY: style
style:
	@poetry run ruff format ./app
	@poetry run ruff check --select I app/*.py --fix
