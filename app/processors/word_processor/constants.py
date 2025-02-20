from enum import Enum

from models import EnglishWordsDB, UkrainianWordsDB


class Languages(Enum):
    ENGLISH = EnglishWordsDB
    UKRAINIAN = UkrainianWordsDB
