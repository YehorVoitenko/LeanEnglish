import copy

from sqlmodel import Session

from models import UserData
from processors.user_processor.schemas import CreateUserRequest


class CreateUser:
    def __init__(
            self,
            session: Session,
            user_to_create: CreateUserRequest
    ):

        self._session = session
        self._user_to_create = user_to_create


    def process(self):
        new_user = UserData(
            user_id=self._user_to_create.user_id
        )
        self._session.add(new_user)
        self._session.flush()
        created_user = copy.deepcopy(new_user)
        self._session.commit()

        return created_user
