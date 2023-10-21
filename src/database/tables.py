import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class User(Base):
    __tablename__ = "User"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(150), unique=True, nullable=False)
    email = sa.Column(sa.String(150), unique=True, nullable=False)
    password = sa.Column(sa.String(150), nullable=False)
    score = sa.Column(sa.Integer, nullable=False)
    inventory = relationship("Inventory")


class Inventory(Base):
    __tablename__ = "Inventory"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("User.id"))
    plant_id = sa.Column(sa.Integer, sa.ForeignKey("Plant.id"))
    photo_id = sa.Column(sa.Integer, sa.ForeignKey("Photo.id"))
    weight = sa.Column(sa.Integer, nullable=False)
    age = sa.Column(sa.Integer, nullable=False)
    height = sa.Column(sa.Integer, nullable=False)


class Plant(Base):
    __tablename__ = "Plant"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(150), nullable=False, unique=True)
    co2_absorbtion = sa.Column(sa.Numeric, nullable=False)
    formula = sa.Column(sa.String(100), nullable=False)
    inventory = relationship("Inventory")


class Photo(Base):
    __tablename__ = "Photo"

    id = sa.Column(sa.Integer, primary_key=True)
    blob = sa.Column(sa.LargeBinary, nullable=False, unique=True)
    inventory = relationship("Inventory")


class Model(Base):
    __tablename__ = "Model"

    id = sa.Column(sa.Integer, primary_key=True)
    blob = sa.Column(sa.LargeBinary, nullable=False, unique=True)
