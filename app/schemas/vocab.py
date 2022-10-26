from pydantic import BaseModel


class VocabBase(BaseModel):
    vocab: str


class UpdateVocabObject(VocabBase):
    vocab: str
