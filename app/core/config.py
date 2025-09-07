import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/v1"
    APP_VERSION: str = os.environ.get("APP_VERSION", "dev")
    DB_HOST: str = os.environ.get("DB_HOST", "localhost")
    DB_PORT: int = os.environ.get("DB_PORT", 5432)
    DB_USER: str = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD", "postgres")
    DB_NAME: str = os.environ.get("DB_NAME", "demo")
    DB_DSN: str = os.environ.get(
        "DB_DSN",
        (f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"),
    )


settings = Settings()
