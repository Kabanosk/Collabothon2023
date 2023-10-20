from sqlalchemy import Column, Integer, String, Table, MetaData

metadata = MetaData()

User = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("email", String, nullable=False),
)