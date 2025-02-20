from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from processors.user_processor.processor import CreateNewUser
from processors.user_processor.schemas import CreateUserRequest
from services.database_service import get_database_session

user_router = APIRouter(
    tags=['Users'],
    prefix='/user'
)


@user_router.post('/create_new_user')
def create_new_user(
        request: CreateUserRequest,
        session: Session = Depends(get_database_session),
):
    task = CreateNewUser(
        session=session,
        user_to_create=request
    )
    return task.process()
