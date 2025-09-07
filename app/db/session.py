from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.DB_DSN)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
