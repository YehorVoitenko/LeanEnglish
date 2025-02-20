from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlmodel import SQLModel

from config.database_config import DATABASE_URL

engine = create_engine(
    url=DATABASE_URL,
    echo=True
)

SQLModel.metadata.create_all(engine)

@contextmanager
def get_database_session():
    session = Session(engine)
    yield session
