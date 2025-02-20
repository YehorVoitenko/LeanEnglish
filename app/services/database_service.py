import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlmodel import SQLModel

from config.database_config import DATABASE_URL

engine = create_engine(
    url=DATABASE_URL,
    echo=True
)

SQLModel.metadata.create_all(engine)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)

def get_database_session():
    session = SessionLocal()
    try:
        yield session

    finally:
        session.close()

def init_tables():
    os.system('alembic upgrade head')
