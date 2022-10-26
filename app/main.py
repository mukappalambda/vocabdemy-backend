from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=api_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"Version": "0.0.1", "Description": "Welcome to Vocabdemy."}
