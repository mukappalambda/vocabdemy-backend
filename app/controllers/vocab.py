from app.models.vocab import Vocab
from app.schema.vocab import VocabBase
from sqlalchemy.orm import Session


class VocabController:
    def __init__(self, database: Session):
        self.database = database

    def get_vocabs(self):
        return self.database.query().all()

    def create_vocab(self, vocab: VocabBase):

        v = Vocab(vocab=vocab.vocab)

        self.database.add(v)
        self.database.commit()

    def delete_vocab(self):
        # TODO
        pass

    def update_vocab(self):
        # TODO
        pass
