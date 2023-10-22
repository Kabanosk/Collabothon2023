import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from database.utils import data_for_model
from model import get_model
from routes.auth import router as auth_router
from routes.inventory import router as plant_router
from routes.user import router as profile_router

load_dotenv()


def create_app() -> FastAPI:
    _app = FastAPI()

    _model = get_model(data_for_model())
    _model.save()

    _app.include_router(auth_router)
    _app.include_router(plant_router, prefix="/inventory")
    _app.include_router(profile_router, prefix="/profile")
    _app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))
    return _app


app = create_app()
