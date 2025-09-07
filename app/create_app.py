from fastapi import APIRouter, FastAPI

from app.db.base import Base
from app.db.session import engine


def create_app(version: str, router: APIRouter, router_prefix: str) -> FastAPI:
    Base.metadata.create_all(bind=engine)

    app = FastAPI(version=version)
    app.include_router(router=router, prefix=router_prefix)

    @app.get("/")
    def read_root():
        return {"Version": version, "Description": "Welcome to Vocabdemy."}

    return app
