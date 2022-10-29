"""
User Router
"""
from typing import List

from app import schemas
from app.api.dependencies import get_db
from app.api.utils import check_obj_or_raise_exception
from app.crud import crud_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=List[schemas.UserInDB])
async def read_users(db: Session = Depends(get_db)):
    """
    Get all users
    """
    objs = crud_user.get_multi(db=db)
    return objs


@router.get("/{id}", response_model=schemas.UserInDB)
async def read_user(db: Session = Depends(get_db), *, id: int):
    """
    Get the user
    """
    obj = crud_user.get(db=db, id=id)
    check_obj_or_raise_exception(obj=obj)
    return obj
