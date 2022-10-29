"""
User Router
"""
from typing import List

from app import schemas
from app.api.dependencies import get_db
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
