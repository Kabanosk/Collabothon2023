"""Create tables

Revision ID: 5b869c42fe65
Revises: 6699e75570d3
Create Date: 2023-10-21 00:58:43.006138

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5b869c42fe65"
down_revision: Union[str, None] = "6699e75570d3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Photo",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("blob", sa.LargeBinary(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "Plant",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("co2_absorbtion", sa.Numeric(), nullable=False),
        sa.Column("formula", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "User",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=150), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=False),
        sa.Column("password", sa.String(length=150), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "Inventory",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("plant_id", sa.Integer(), nullable=True),
        sa.Column("photo_id", sa.Integer(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("height", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["photo_id"],
            ["Photo.id"],
        ),
        sa.ForeignKeyConstraint(
            ["plant_id"],
            ["Plant.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["User.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("Users")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "Users",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('\"Users_id_seq\"'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="Users_pkey"),
    )
    op.drop_table("Inventory")
    op.drop_table("User")
    op.drop_table("Plant")
    op.drop_table("Photo")
    # ### end Alembic commands ###
