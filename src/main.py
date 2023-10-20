from fastapi import FastAPI
from .database.connector import connect_with_connector_auto_iam_authn

def create_app():
    app = FastAPI()



