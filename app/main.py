from typing import Optional

from fastapi import Depends, FastAPI

from app.database import engine, get_db
from app.models.loaded_base import load_models_base

from .routers import vocab

Base = load_models_base()
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(vocab.router)


@app.get("/")
def read_root():
    return {"Version": "0.0.1", "Description": "Welcome to Vocabdemy."}
