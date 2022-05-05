from fastapi import APIRouter, Depends
from app.models.loaded_base import load_models_base
from app.dependencies.controller import get_controller
from app.database import database
from app.controllers import vocab as vocab_

router = APIRouter(
    prefix="/vocabs"
)
Base = load_models_base()


@router.get("/")
def read_vocabs(controller=Depends(get_controller(database, vocab_.VocabController))):
    return controller.get_vocabs()


@router.post("/")
def create_vocab(vocab: str, controller=Depends(get_controller(database, vocab_.VocabController))):
    return controller.create_vocab()
