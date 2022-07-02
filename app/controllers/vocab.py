from app.models.vocab import Vocab
from app.schema.vocab import UpdateVocabObject, VocabBase
from sqlalchemy.orm import Session


class VocabController:
    def __init__(self, database: Session):
        self.database = database

    def get_vocabs(self):
        return self.database.query(Vocab).all()

    def create_vocab(self, vocab: VocabBase):

        v = Vocab(vocab=vocab.vocab)

        self.database.add(v)
        self.database.commit()

    def delete_vocab(self, id: int):
        """
        Receive an id and remove the data
        """
        self.database.query(Vocab).filter(Vocab.id == id).delete()

        self.database.commit()

    def update_vocab(self, vocab_object: UpdateVocabObject, id: int):
        """
        Receive vocab id and get the data
        """
        vocab = self.database.query(Vocab).get(id)

        for column_name, value in vocab_object:
            setattr(vocab, column_name, value)

        self.database.commit()
