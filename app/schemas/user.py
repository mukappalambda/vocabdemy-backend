from datetime import datetime
from typing import Union

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: str
    name: str
    username: str


class UserRead(UserBase):
    created_at: Union[datetime, None]


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int = Field(example=1)
    created_at: datetime = Field(example=datetime.utcnow())
    updated_at: Union[datetime, None]

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    pass
