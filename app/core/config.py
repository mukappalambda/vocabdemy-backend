import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/v1"
    POSTGRES_SERVER = os.environ.get("POSTGRES_SERVER", "postgres")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "demo")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
