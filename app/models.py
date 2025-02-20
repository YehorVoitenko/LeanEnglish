from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class UserData(SQLModel, table=True):
    user_id: str = Field(primary_key=True)

    english_words: List["EnglishWordsDB"] = Relationship(back_populates="user")
    ukrainian_words: List["UkrainianWordsDB"] = Relationship(back_populates="user")
    translations: List["Translations"] = Relationship(back_populates="user")  # Add this


class EnglishWordsDB(SQLModel, table=True):
    origin_word: str = Field(primary_key=True)
    user_id: str = Field(foreign_key="userdata.user_id", primary_key=True)

    user: Optional[UserData] = Relationship(back_populates="english_words")


class UkrainianWordsDB(SQLModel, table=True):
    origin_word: str = Field(primary_key=True)
    user_id: str = Field(foreign_key="userdata.user_id", primary_key=True)

    user: Optional[UserData] = Relationship(back_populates="ukrainian_words")


class Translations(SQLModel, table=True):
    origin_word: str = Field(primary_key=True)
    translation: str = Field(primary_key=True)
    user_id: str = Field(foreign_key="userdata.user_id", primary_key=True)

    user: Optional[UserData] = Relationship(back_populates="translations")  # Fix this
