from fastapi import FastAPI

from processors.word_processor.routers import word_router
from processors.user_processor.routers import user_router
from services.database_service import init_tables

app = FastAPI()


app.include_router(word_router)
app.include_router(user_router)

init_tables()