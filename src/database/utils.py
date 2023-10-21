from connector import connect_with_connector_auto_iam_authn
from sqlalchemy import insert
from tables import User


# User
# def get_user_by_username(username: str):
#         with engine.connect() as conn:
#             res = conn.execute(f'SELECT * FROM "user" WHERE username = {username}')
#             if res:
#                 return res[0]
#             else:
#                 return None

#
# def get_user_by_email(email: str) -> Optional[None, list]:
#     with connect_with_connector_auto_iam_authn() as engine:
#         with engine.connect() as conn:
#             res = conn.execute(f'SELECT * FROM "user" WHERE email = {email}')
#             if res:
#                 return res[0]
#             else:
#                 return None
#
#
# def get_next_uid() -> int:
#     with connect_with_connector_auto_iam_authn() as engine:
#         with engine.connect() as conn:
#             res = conn.execute(f'SELECT id FROM "user"')
#             return res[-1]
#


def add_user(username, email, password):
    pool = connect_with_connector_auto_iam_authn()

    with pool.connect() as conn:
        query = insert(User).values(username=username, password=password, email=email)
        conn.execute(query)
        conn.commit()
