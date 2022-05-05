from sqlalchemy import Column, Integer, String

from ..database import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
