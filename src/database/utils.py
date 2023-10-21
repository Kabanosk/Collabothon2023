from connector import connect_with_connector
from sqlalchemy import insert, select, update
from tables import Badges, Inventory, Model, Photo, Plant, User, UsersBadges

pool = connect_with_connector()


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


def add_user(username, email, password, score):
    with pool.connect() as conn:
        query = insert(User).values(
            username=username, password=password, email=email, score=score
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
            weight=weight,
            age=age,
            height=height,
        )
        conn.execute(query)
        conn.commit()


def data_for_model():
    with pool.connect() as conn:
        query = select(Inventory.plant_id).join(User, User.id == Inventory.user_id)
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
        query = select(UsersBadges.blob).where(user_id == UsersBadges.user_id)
        ans = conn.execute(query).fetchall()
        conn.commit()

    return ans


def add_badge_to_db(blob):
    with pool.connect() as conn:
        query = insert(Badges).values(
            blob=blob,
        )
        conn.execute(query)
        conn.commit()


def get_model():
    with pool.connect() as conn:
        query = select(Model.blob)
        ans = conn.execute(query).fetchall()
        conn.commit()

    return ans


def update_model(blob):
    with pool.connect() as conn:
        query = update(Model.blob).where(Model.id == 1)
        conn.execute(query)
        conn.commit()


def add_model(blob):
    with pool.connect() as conn:
        query = insert(Model).values(
            blob=blob,
        )
        conn.execute(query)
        conn.commit()
