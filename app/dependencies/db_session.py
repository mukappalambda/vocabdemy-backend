from sqlalchemy.orm import Session
from app.database import database


def get_db_session():
    db = database.sessions_local()
    try:
        yield db
    finally:
        db.close()
