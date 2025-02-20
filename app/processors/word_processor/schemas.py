from pydantic import BaseModel

from processors.word_processor.constants import AvailableLanguages


class WordToCreateRequest(BaseModel):
    user_id: str
    word_to_create: str
    translation: str
    original_language: AvailableLanguages
    translation_language: AvailableLanguages


class CreateWordRequest(BaseModel):
    user_id: str
    word_to_create: str
