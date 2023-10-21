"""Update tables

Revision ID: f75f245352ee
Revises: fb189febb729
Create Date: 2023-10-21 20:45:01.062731

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f75f245352ee"
down_revision: Union[str, None] = "fb189febb729"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "Inventory", sa.Column("creation_date", sa.DateTime(), nullable=False)
    )
    op.add_column("Plant", sa.Column("oxygen_emission", sa.Numeric(), nullable=True))
    op.add_column("User", sa.Column("country", sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("User", "country")
    op.drop_column("Plant", "oxygen_emission")
    op.drop_column("Inventory", "creation_date")
    # ### end Alembic commands ###
