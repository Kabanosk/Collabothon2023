from connector import connect_with_connector_auto_iam_authn
from sqlalchemy import insert, select
from tables import User


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


