import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

from database.utils import data_for_model
from model import get_model
from routes.auth import router as auth_router
from routes.inventory import router as plant_router
from routes.user import router as profile_router
from routes.view import router as view_router

load_dotenv()


def create_app() -> FastAPI:
    _app = FastAPI()
    _model = get_model(data_for_model())
    _model.save()
    _app.include_router(view_router)
    _app.include_router(auth_router)
    _app.include_router(plant_router, prefix="/inventory")
    _app.include_router(profile_router, prefix="/profile")
    _app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))
    _app.mount('/static',StaticFiles(directory='/app/static'),name='static')
    return _app


app = create_app()
