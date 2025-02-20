
from pydantic import BaseModel



class WordToCreateRequest(BaseModel):
    word_to_create: str
    user_id: str
    translation: str
