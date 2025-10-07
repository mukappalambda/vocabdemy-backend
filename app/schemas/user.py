import datetime

try:
    UTC = datetime.UTC
except AttributeError:
    UTC = datetime.timezone.utc

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    email: str
    name: str
    username: str


class UserRead(UserBase):
    created_at: Union[datetime.datetime, None] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int = Field(examples=[1])
    created_at: datetime.datetime = Field(examples=[datetime.datetime.now(UTC)])
    updated_at: Union[datetime.datetime, None] = None
    model_config = ConfigDict(from_attributes=True)


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    pass
