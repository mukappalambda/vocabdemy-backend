from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Group(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
