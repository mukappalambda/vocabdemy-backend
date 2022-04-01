.PHONY: clean
clean:
	find . | grep -E "__pycache__" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf

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
	docker-compose -f docker-compose-dev.yml up -d

.PHONY: prod
prod:
	docker-compose up -d