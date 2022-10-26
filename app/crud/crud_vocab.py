from typing import List

from app.models.vocab import Vocab
from app.schemas.vocab import UpdateVocabObject, VocabBase
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def get_multi(db: Session) -> List[Vocab]:
    return db.query(Vocab).all()


def get(db: Session, sensor_id: str) -> Vocab:
    return db.query(Vocab).filter(Vocab.id == sensor_id).first()


def create(db: Session, vocab_in: VocabBase) -> Vocab:
    vocab_dict = jsonable_encoder(vocab_in)
    obj = Vocab(**vocab_dict)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, id: int, vocab_in: Vocab) -> Vocab:
    """
    Receive vocab id and get the data
    """
    vocab = db.query(Vocab).get(id)

    for k, v in vocab_in:
        setattr(vocab, k, v)

    db.commit()
    return vocab


def delete(db: Session, id: int) -> Vocab:
    obj: Vocab = db.query(Vocab).filter(Vocab.id == id).first()
    db.delete(obj)
    db.commit()
    return obj
