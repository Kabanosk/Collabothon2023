from sqlalchemy import Column, BigInteger, String, Table, MetaData

metadata = MetaData()

User = Table(
    "User",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("email", String, nullable=False),
)