from typing import Optional

from fastapi import Depends, FastAPI

from app.database import engine, get_db
from app.models.loaded_base import load_models_base

Base = load_models_base()
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}


@app.get("/users/{id}")
def read_users(user_id, db = Depends(get_db)):
  return 
