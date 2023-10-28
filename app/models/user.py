from sqlalchemy import TIMESTAMP, Column, Integer, String, text

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30))
    password = Column(String(30))
    email = Column(String(30))
    name = Column(String(30))
    created_at = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)

    def __repr__(self) -> str:
        return f"<User(id={self.id}; username={self.username}; email={self.email}; name={self.name}; created_at={self.created_at})>"
