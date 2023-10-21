from fastapi import FastAPI
from database.connector import connect_with_connector

app = FastAPI()

pool = connect_with_connector()


@app.get("/")
def main():
    return {"success": True}
