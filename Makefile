.PHONY: clean
clean:
	@find ./app -name "__pycache__" | xargs rm -rf
	@find ./app -name ".pytest_cache" | xargs rm -rf

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

.PHONY: dev
dev:
	docker-compose -f docker-compose-dev.yml up

.PHONY: prod
prod:
	docker-compose up -d

.PHONY: style
style:
	isort --profile black . && black .
