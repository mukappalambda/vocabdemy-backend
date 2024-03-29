ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION} as build

RUN pip install --upgrade pip \
    && apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev build-essential

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get autoremove -y gcc build-essential \
    && apt-get clean -y \
    && rm -rf /root/.cache \
    && rm -rf /var/apt/lists/* \
    && rm -rf /var/cache/apt/*

FROM python:${PYTHON_VERSION}

ARG APP_VERSION
ENV APP_VERSION=${APP_VERSION}

RUN apt-get update \
    && apt-get install -y libpq-dev \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /code

COPY entrypoint.sh /code/entrypoint.sh
COPY  app/ /code/app/

EXPOSE 8000

CMD ["bash", "./entrypoint.sh"]
