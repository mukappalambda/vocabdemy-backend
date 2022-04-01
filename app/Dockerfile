ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

WORKDIR /code/src

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && apt-get update \
    && apt-get install --yes --no-install-recommends \
    gcc g++ libffi-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get autoremove --yes gcc g++ libffi-dev \
    && apt-get clean

USER root

ENV PATH="/root/.local/bin:${PATH}"
COPY  src/ /code/src
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]