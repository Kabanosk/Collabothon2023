from dataclasses import dataclass

import sqlalchemy


@dataclass
class User:
    id: int
    login: str
    password: str
    email: str

    def insert_to_db(self):
        pass

    def add_image(self):
        pass
