from app.models.vocab import Vocab


class VocabController:
    def __init__(self, database):
        self.database = database

    def get_vocabs(self):
        return self.database.query(Vocab).all()

    def create_vocab(self):
        # TODO
        pass

    def delete_vocab(self):
        # TODO
        pass

    def update_vocab(swlf):
        # TODO
        pass
