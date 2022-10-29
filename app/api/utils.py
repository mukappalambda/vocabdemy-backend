from app.schemas import UserInDB
from fastapi import HTTPException, status


def check_obj_or_raise_exception(obj: UserInDB):
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instance not found",
        )
