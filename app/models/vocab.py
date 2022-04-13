from sqlalchemy import Column, Integer, String

from ..database import Base


class Vocab(Base):
  __tablename__ = "vocabs"

  id = Column(Integer, primary_key= True)
  vocab = Column(String(30))
