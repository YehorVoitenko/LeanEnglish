import copy
from enum import Enum
from typing import Type

from sqlmodel import Session

from models import Translations
from processors.word_processor.constants import AvailableLanguages
from processors.word_processor.schemas import WordToCreateRequest, CreateWordRequest
from processors.word_processor.utils import CreateEnglishWord, CreateUkrainianWord, CreateWord


class LanguageProcessor(Enum):
    ENGLISH: Type[CreateWord] = CreateEnglishWord
    UKRAINIAN: Type[CreateWord] = CreateUkrainianWord


class CreateNewWord:
    def __init__(
            self,
            session: Session,
            request: WordToCreateRequest
    ) -> None:
        self._request: WordToCreateRequest = request
        self._session: Session = session

    @staticmethod
    def _determine_processor_by_language(
            requested_language: AvailableLanguages
    ) -> Type[CreateWord]:
        return LanguageProcessor[requested_language.name].value

    def _create_original_word(self):
        processor_class = self._determine_processor_by_language(
            requested_language=self._request.original_language
        )

        processor = processor_class(
            session=self._session,
            word_to_create=CreateWordRequest(
                user_id=self._request.user_id,
                word_to_create=self._request.word_to_create
            )
        )
        return processor.process()

    def _create_translation_word(self):
        processor_class = self._determine_processor_by_language(
            requested_language=self._request.translation_language
        )

        processor = processor_class(
            session=self._session,
            word_to_create=CreateWordRequest(
                user_id=self._request.user_id,
                word_to_create=self._request.translation
            )
        )
        return processor.process()

    def _create_link(
            self,
            origin_word: str,
            translation_word: str
    ) -> Translations:
        full_translation = Translations(
            origin_word=origin_word,
            translation=translation_word,
            user_id=self._request.user_id
        )
        self._session.add(full_translation)
        self._session.flush()

        return copy.deepcopy(full_translation)

    def process(self) -> Translations:
        origin_word = self._create_original_word().origin_word
        translation = self._create_translation_word().origin_word

        full_info = self._create_link(
            origin_word=origin_word,
            translation_word=translation
        )

        self._session.commit()

        return full_info
