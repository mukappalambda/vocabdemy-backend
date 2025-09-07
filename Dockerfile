ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION:-3.13.7-slim} AS build

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade pip==25.2 \
    && pip install --no-cache-dir -r /requirements.txt

FROM python:${PYTHON_VERSION:-3.13.7-slim}

ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}

COPY --from=build /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /code

COPY entrypoint.sh /code/entrypoint.sh
COPY app/ /code/app/

EXPOSE 8000

CMD ["bash", "./entrypoint.sh"]
