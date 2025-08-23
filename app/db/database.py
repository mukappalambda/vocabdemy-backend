from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.db.session import engine


class Database:
    """Mock database class for example."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""
        Base.metadata.create_all(bind=engine)
        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""

    def get_session_maker(self):
        """Get a new session maker."""
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)
