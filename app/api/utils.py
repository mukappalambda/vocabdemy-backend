from typing import Optional

from fastapi import HTTPException, status

from app.schemas import UserInDB


def check_obj_or_raise_exception(obj: Optional[UserInDB]):
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instance not found",
        )
