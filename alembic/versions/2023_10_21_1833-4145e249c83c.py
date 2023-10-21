"""Add score

Revision ID: 4145e249c83c
Revises: b91f5a2abba6
Create Date: 2023-10-21 18:33:25.949557

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4145e249c83c"
down_revision: Union[str, None] = "b91f5a2abba6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("User", sa.Column("score", sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("User", "score")
    # ### end Alembic commands ###
