from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, uri):
        self.uri = uri
        self.sessions_local = None
        self.engine = None

    def create_engine(self):
        self.engine = create_engine(self.uri)

    def get_base(self):
        return declarative_base()

    def create_sessions_local(self):
        self.sessions_local = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.sessions_local()
        try:
            yield db
        finally:
            db.close()


# init
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/demo"
database = Database(SQLALCHEMY_DATABASE_URL)
database.create_engine()
database.create_sessions_local()

# export
engine = database.engine
Base = database.get_base()
get_db = database.get_db
