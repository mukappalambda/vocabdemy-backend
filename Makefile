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
build: test tmp_build

.PHONY: tmp_build
tmp_build:
	docker-compose build

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

.PHONY: dev
dev:
	docker-compose -f docker-compose-dev.yml up

.PHONY: prod
prod:
	docker-compose up -d

.PHONY: style
style:
	isort --profile black . && black .
