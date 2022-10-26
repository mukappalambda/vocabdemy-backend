from app.db.base_class import Base
from sqlalchemy import Column, Integer, String


class Group(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
