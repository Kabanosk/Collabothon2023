from connector import connect_with_connector_auto_iam_authn
from sqlalchemy import insert, select, join
from tables import User, Inventory
# from model import get_model


def get_user_by_username(username: str):
    pool = connect_with_connector_auto_iam_authn()

    with pool.connect() as conn:
        query = select(User).where(User.username == username)
        result = conn.execute(query).fetchone()

        return result


def get_user_by_email(email: str):
    pool = connect_with_connector_auto_iam_authn()

    with pool.connect() as conn:
        query = select(User).where(User.email == email)
        result = conn.execute(query).fetchone()

        return result


def add_user(username, email, password):
    pool = connect_with_connector_auto_iam_authn()

    with pool.connect() as conn:
        query = insert(User).values(username=username, password=password, email=email)
        conn.execute(query)
        conn.commit()


def add_plant(user_id, plant_id, photo_id, weight=0, age=0, height=0):
    pool = connect_with_connector_auto_iam_authn()

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


def creating_model():
    pool = connect_with_connector_auto_iam_authn()

    with pool.connect() as conn:
        query = select(Inventory.id, Inventory.plant_id).select_from(User).join(Inventory, User.id == Inventory.user_id)
        conn.execute(query)
        conn.commit()

    # model = get_model()


creating_model()

