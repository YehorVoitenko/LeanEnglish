import copy

from sqlmodel import Session

from processors.word_processor.constants import LanguagesDatabases
from processors.word_processor.schemas import WordToCreateRequest, CreateWordRequest


class CreateWord:
    def __init__(
            self,
            session: Session,
            word_to_create: CreateWordRequest,
            language: LanguagesDatabases,
    ):
        self._language = language
        self._word_to_create = word_to_create
        self._session = session

    def process(self):
        new_word = self._language.value(
            origin_word=self._word_to_create.word_to_create,
            user_id=self._word_to_create.user_id
        )

        self._session.add(new_word)
        self._session.flush()

        created_word = copy.deepcopy(new_word)

        return created_word


class CreateEnglishWord(CreateWord):
    def __init__(
            self,
            session: Session,
            word_to_create: CreateWordRequest,
    ):
        super().__init__(
            session=session,
            word_to_create=word_to_create,
            language=LanguagesDatabases.ENGLISH
        )


class CreateUkrainianWord(CreateWord):
    def __init__(
            self,
            session: Session,
            word_to_create: CreateWordRequest
    ):
        super().__init__(
            session=session,
            word_to_create=word_to_create,
            language=LanguagesDatabases.UKRAINIAN
        )
