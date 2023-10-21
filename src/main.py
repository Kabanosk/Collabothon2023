from fastapi import FastAPI
from src.database.connector import connect_with_connector

app = FastAPI()

pool = connect_with_connector()


@app.get("/")
def main():
    return {"success": True}
