from fastapi import FastAPI

from routes.user import router as profile_router


def create_app() -> FastAPI:
    _app = FastAPI()

    _app.include_router(
        profile_router,
        prefix='/profile'
    )
    return _app


app = create_app()
