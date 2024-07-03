# Vocabdemy Backend

A Python App for Vocabulary Memorizer

[![CircleCI](https://circleci.com/gh/mukappalambda/vocabdemy-backend.svg?style=shield)](https://circleci.com/gh/mukappalambda/vocabdemy-backend)

```
                                                   __        __
                           _   ______  _________ _/ /_  ____/ /__  ____ ___  __  __
                          | | / / __ \/ ___/ __ `/ __ \/ __  / _ \/ __ `__ \/ / / /
                          | |/ / /_/ / /__/ /_/ / /_/ / /_/ /  __/ / / / / / /_/ /
                          |___/\____/\___/\__,_/_.___/\__,_/\___/_/ /_/ /_/\__, /
                                                                          /____/

```

---

```bash
git clone git@github.com:mukappalambda/vocabdemy-backend.git
```

```bash
cd vocabdemy-backend
```

---

## Install Project Dependencies

After having [poetry](https://github.com/python-poetry/poetry) installed on your machine, run:

```bash
make install
```

---
## Development Mode

```bash
make env
make dev
```

This project uses [poetry](https://github.com/python-poetry/poetry) to manage dependencies.

For the purpose of future reference, the following are steps to add or remove certain package:

```bash
poetry add <some_python_package>
make poetry-lock && make poetry-export
```

**Build the Docker Image**

```bash
make env
make build
make images-filter
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
vocabdemy    0.1.0     9d094976ca7e   12 seconds ago   1.02GB
```

---

## Production Mode

```bash
make env
make prod
docker compose ps
  Name                Command               State           Ports         
--------------------------------------------------------------------------
pgweb      /usr/bin/pgweb --bind=0.0. ...   Up      0.0.0.0:8081->8081/tcp
postgres   docker-entrypoint.sh postgres    Up      0.0.0.0:5432->5432/tcp
python     uvicorn app.main:app --hos ...   Up      0.0.0.0:8000->8000/tcp
# tear down the stack
$ docker-compose down -v --timeout 1
```

## Test

```bash
curl localhost:8000
```
