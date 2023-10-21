from fastapi import FastAPI

app = FastAPI()


def create_app() -> FastAPI:
    app = FastAPI()

    return app

