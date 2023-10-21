from fastapi import FastAPI
from database import pool

app = FastAPI()


@app.get("/")
def main():
    return {"success": True}
