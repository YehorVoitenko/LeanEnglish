import copy

from sqlmodel import Session

from models import Translations
from processors.word_processor.constants import Languages
from processors.word_processor.schemas import WordToCreateRequest


class CreateWord:
    def __init__(
            self,
            session: Session,
            word_to_create: WordToCreateRequest,
            language: Languages,
    ):
        self._language = language
        self._word_to_create = word_to_create
        self._session = session

    def process(self):
        new_word = self._language.value(
            original_word=self._word_to_create.word_to_create,
            user_id=self._word_to_create.user_id,
            origin_word='origin'
        )

        self._session.add(new_word)
        self._session.flush()

        translation = Translations(
            origin_word=self._word_to_create.word_to_create,
            translation=self._word_to_create.word_to_create + "translation"
        )

        self._session.add_all([new_word, translation])
        self._session.flush()

        created_word = copy.deepcopy(new_word)
        self._session.commit()

        return created_word
