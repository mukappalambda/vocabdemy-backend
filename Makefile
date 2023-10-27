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
	@docker compose build

.PHONY: build-dev
build-dev:
	@PYTHON_VERSION=$$(grep PYTHON_VERSION .env | tr -d PYTHON_VERSION=); \
	docker build -t vocabdemy:test -f Dockerfile.dev --build-arg PYTHON_VERSION=$${PYTHON_VERSION} .

.PHONY: test
test: tmp_test clean

.PHONY: tmp_test
tmp_test:
	cd ./app/src && pytest && cd ..

.PHONY: poetry-lock
poetry-lock:
	@poetry lock --no-update

.PHONY: poetry-export
poetry-export:
	@poetry export -o requirements.txt --without-hashes

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
	isort --profile black . && black .
