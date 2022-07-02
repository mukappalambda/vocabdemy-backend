from app import schema
from app.controllers import vocab as vocab_
from app.dependencies.controller import get_controller
from app.models.loaded_base import load_models_base
from app.models.vocab import Vocab
from fastapi import APIRouter, Depends, Response, status

router = APIRouter(
    prefix="/vocabs"
)
Base = load_models_base()


@router.get("")
def read_vocabs(controller=Depends(get_controller(vocab_.VocabController))):
    return controller.get_vocabs()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_vocab(
        vocab: schema.VocabBase,
        controller=Depends(get_controller(vocab_.VocabController)),
):
    try:
        controller.create_vocab(vocab)
    except Exception as e:
        print(e, "Vocab creation failed")
        # TODO add status code

    return "Create successfully."


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_vocab(
    id: int,
    vocab: schema.UpdateVocabObject,
    controller: vocab_.VocabController = Depends(
        get_controller(vocab_.VocabController))
):
    try:
        controller.update_vocab(vocab, id)
    except Exception as e:
        print(e, f"Something went wrong when updating Vocab {id}.")
    return "Update {id} successfully."
