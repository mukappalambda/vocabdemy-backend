from pydantic import BaseModel


class VocabBase(BaseModel):
    vocab: str
