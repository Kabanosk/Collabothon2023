from fastapi import FastAPI
from database.connector import connect_with_connector

from routes.auth import router as auth_router


def create_app() -> FastAPI:
    _app = FastAPI()

    _app.include_router(auth_router)
    return _app


app = create_app()
