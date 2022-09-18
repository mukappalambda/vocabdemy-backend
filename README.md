# Vocabdemy Backend

A Python App for Vocabulary Memorizer

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

## Development Mode

```bash
cp .env{.example,}
make dev
```

This project uses [poetry](https://github.com/python-poetry/poetry) to manage depedencies.

For the purpose of future reference, the following are steps to add or remove certain package:

```bash
poetry add <some_python_package>
poetry export -o requirements.txt --without-hashes
# remember to version control these files: poetry.lock, pyproject.toml, requirements.txt
```

---

## Production Mode

```bash
cp .env{.example,}
make prod
```

## Test

```bash
curl localhost:8000
```
