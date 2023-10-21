import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from routes.auth import router as auth_router

load_dotenv()


def create_app() -> FastAPI:
    _app = FastAPI()

    _app.include_router(auth_router)
    _app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))
    return _app


app = create_app()
