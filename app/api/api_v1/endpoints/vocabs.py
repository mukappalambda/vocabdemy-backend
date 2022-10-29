"""
Vocab Router
"""
from app import schemas
from app.api.dependencies import get_db
from app.crud import crud_vocab
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("")
async def read_vocabs(db: Session = Depends(get_db)):
    vocabs = crud_vocab.get_multi(db=db)
    return vocabs


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_vocab(
    db: Session = Depends(get_db),
    *,
    vocab: schemas.VocabBase,
):
    """
    Add a vocab
    """
    try:
        crud_vocab.create(db=db, vocab_in=vocab)
    except Exception as e:  # pylint: disable=broad-except
        print(e, "Vocab creation failed")
        # TODO add status code

    return "Create successfully."


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_vocab(
    db: Session = Depends(get_db),
    *,
    id: int,
    vocab: schemas.UpdateVocabObject,
):
    """
    Update the data of vocab
    """
    try:
        # controller.update_vocab(vocab, id)
        crud_vocab.update(db=db, id=id, vocab_in=vocab)
    except Exception as e:  # pylint: disable=broad-except
        print(e, f"Something went wrong when updating Vocab {id}.")
    return "Update {id} successfully."


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_vocab(
    db: Session = Depends(get_db),
    *,
    id: int,
):
    """
    Delete a vocab
    """
    try:
        crud_vocab.delete(db=db, id=id)
    except Exception as e:  # pylint: disable=broad-except
        print(e, f"Something went wrong when deleting Vocab {id}.")
    return "Delete {id} successfully."
