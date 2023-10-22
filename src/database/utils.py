import datetime

from sqlalchemy import insert, select, update

from .connector import connect_with_connector
from .tables import Badges, Inventory, Photo, Plant, User, UsersBadges

pool = connect_with_connector()


def get_plant_stats(user_id):
    with pool.connect() as conn:
        query = select(Inventory.creation_date, Plant.co2_absorbtion, Plant.oxygen_emission).
        join(Plant, Plant.id == Inventory.plant_id).
        where(Inventory.user_id == user_id).order_by(Inventory.creation_date.asc())
        result = conn.execute(query).fetchall()
    return result


def get_user_by_username(username: str):
    with pool.connect() as conn:
        query = select(User).where(User.username == username)
        result = conn.execute(query).fetchone()
    return result


def get_user_by_email(email: str):
    with pool.connect() as conn:
        query = select(User).where(User.email == email)
        result = conn.execute(query).fetchone()
    return result


def add_user(username, email, password, score, country=None):
    with pool.connect() as conn:
        query = insert(User).values(
            username=username,
            password=password,
            email=email,
            score=score,
            country=country,
        )
        conn.execute(query)

        conn.commit()


def add_plant(name, co, formula):
    with pool.connect() as conn:
        query = insert(Plant).values(
            name=name,
            co2_absorbtion=co,
            formula=formula,
        )
        conn.execute(query)
        conn.commit()


def add_photo(blob):
    with pool.connect() as conn:
        query = insert(Photo).values(
            blob=blob,
        )
        conn.execute(query)
        conn.commit()


def add_plant_to_inventory(user_id, plant_id, photo_id, weight=0, age=0, height=0):
    with pool.connect() as conn:
        query = insert(Inventory).values(
            user_id=user_id,
            plant_id=plant_id,
            photo_id=photo_id,
            creation_date=datetime.datetime.now(),
            weight=weight,
            age=age,
            height=height,
        )
        conn.execute(query)
        conn.commit()


def data_for_model():
    with pool.connect() as conn:
        query = select(User.id, Inventory.plant_id).join(
            User, User.id == Inventory.user_id
        )
        ans = conn.execute(query).fetchall()
        conn.commit()
    return ans


def add_user_badge(blob, user_id):
    with pool.connect() as conn:
        query = insert(UsersBadges).values(
            blob=blob,
            user_id=user_id,
        )
        conn.execute(query)
        conn.commit()


def get_user_badge(user_id):
    with pool.connect() as conn:
        query = (
            select(Badges.path)
            .join(UsersBadges, UsersBadges.blob_id == Badges.id)
            .join(User, User.id == UsersBadges.user_id).where(User.id == user_id)
        )
        ans = conn.execute(query).fetchall()
        conn.commit()
    return ans


def add_badge_to_db(blob, name):
    with pool.connect() as conn:
        query = insert(Badges).values(
            path=blob,
            description=name,
        )
        conn.execute(query)
        conn.commit()


def get_all_plants_from_db():
    with pool.connect() as conn:
        query = select(Plant)
        ans = conn.execute(query).fetchall()
        conn.commit()
    return ans


def get_plant_by_name(name: str):
    with pool.connect() as conn:
        query = select(Plant).where(Plant.name == name)
        result = conn.execute(query).fetchone()
    return result
