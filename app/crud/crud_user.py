from typing import List

from app.models.user import User
from app.schemas.user import UserInDB
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
