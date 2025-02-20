from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    user_id: str