from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from processors.word_processor.processor import CreateNewWord
from processors.word_processor.schemas import WordToCreateRequest
from services.database_service import get_database_session

word_router = APIRouter(
    tags=['Words'],
    prefix='/words'
)


@word_router.post('/create_new_word')
def create_new_word(
        request: WordToCreateRequest,
        session: Session = Depends(get_database_session),
):
    task = CreateNewWord(
        session=session,
        request=request
    )
    return task.process()
