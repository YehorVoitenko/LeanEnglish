import datetime
import os

from database import get_database_session
from processors.user_processor.processor import CreateUser
from processors.user_processor.schemas import CreateUserRequest
from processors.word_processor.constants import Languages
from processors.word_processor.processor import CreateWord
from processors.word_processor.schemas import WordToCreateRequest

os.system('alembic upgrade head')

with get_database_session() as session:
    user_id = str(datetime.datetime.now())
    create_user = CreateUser(
        session=session,
        user_to_create=CreateUserRequest(user_id=user_id)
    )

    create_user.process()

    create_word = CreateWord(
        session=session,
        word_to_create=WordToCreateRequest(word_to_create='sdfxsdf', user_id=user_id, translation='sdfxsdf'),
        language=Languages.ENGLISH
    )
    create_word.process()
