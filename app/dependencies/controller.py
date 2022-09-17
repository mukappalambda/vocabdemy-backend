from fastapi import Depends
from app.dependencies.db_session import get_db_session
from sqlalchemy.orm import Session


def get_controller(controller):
    def _get_controller(db: Session = Depends(get_db_session)):
        yield controller(db)

    return _get_controller
