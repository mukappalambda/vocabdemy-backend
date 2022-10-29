from typing import List

from app.models.user import User
from app.schemas.user import UserCreate, UserInDB
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def get_multi(db: Session) -> List[UserInDB]:
    """
    Examples
    --------
    >>> users = get_multi(db=db)
    """
    objs = db.query(User).all()
    for obj in objs:
        print(obj)
    return objs


def get(db: Session, id: int) -> UserInDB:
    """
    Examples
    --------
    >>> user = get(db=db)
    """
    obj = db.query(User).get(id)
    return obj


def create(db: Session, obj_in: UserCreate) -> UserInDB:
    """
    Examples
    --------
    >>> user = create(db=db, obj_in=obj_in)
    """
    obj_dict = jsonable_encoder(obj_in)
    obj = User(**obj_dict)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
