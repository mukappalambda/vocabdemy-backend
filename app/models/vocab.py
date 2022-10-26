from app.db.base_class import Base
from sqlalchemy import Column, Integer, String


class Vocab(Base):

    id = Column(Integer, primary_key=True)
    vocab = Column(String(30))
