"""
Vocab Router
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.api.dependencies import get_db
from app.crud import crud_vocab

router = APIRouter()


@router.get("")
async def read_vocabs(db_session: Session = Depends(get_db)):
    """
    Get all vocabs
    """
    vocabs = crud_vocab.get_multi(db=db_session)
    return vocabs


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_vocab(
    db_session: Session = Depends(get_db),
    *,
    vocab: schemas.VocabBase,
):
    """
    Add a vocab
    """
    try:
        crud_vocab.create(db=db_session, vocab_in=vocab)
    # pylint: disable=broad-except
    except Exception as e:
        print(e, "Vocab creation failed")
        # TODO add status code

    return "Create successfully."


@router.put("/{vocab_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_vocab(
    db_session: Session = Depends(get_db),
    *,
    vocab_id: int,
    vocab: schemas.UpdateVocabObject,
):
    """
    Update the data of vocab
    """
    try:
        crud_vocab.update(db=db_session, id=vocab_id, vocab_in=vocab)
    # pylint: disable=broad-except
    except Exception as e:
        print(e, f"Something went wrong when updating Vocab {vocab_id}.")
    return f"Update {vocab_id} successfully."


@router.delete("/{vocab_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_vocab(
    db_session: Session = Depends(get_db),
    *,
    vocab_id: int,
):
    """
    Delete a vocab
    """
    try:
        crud_vocab.delete(db=db_session, id=vocab_id)
    # pylint: disable=broad-except
    except Exception as e:
        print(e, f"Something went wrong when deleting Vocab {vocab_id}.")
    return f"Delete {vocab_id} successfully."
