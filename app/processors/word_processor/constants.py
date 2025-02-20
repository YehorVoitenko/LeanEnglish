from enum import Enum
from typing import Type

from models import EnglishWordsDB, UkrainianWordsDB



class LanguagesDatabases(Enum):
    ENGLISH: Type[EnglishWordsDB] = EnglishWordsDB
    UKRAINIAN: Type[UkrainianWordsDB] = UkrainianWordsDB


class AvailableLanguages(Enum):
    ENGLISH = 'ENGLISH'
    UKRAINIAN = 'UKRAINIAN'
