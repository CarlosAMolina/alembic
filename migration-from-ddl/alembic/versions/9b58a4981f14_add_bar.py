"""Add bar

Revision ID: 9b58a4981f14
Revises: b6ff49447f96
Create Date: 2024-07-17 02:11:59.853109

"""

from typing import Sequence
from typing import Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "9b58a4981f14"
down_revision: Union[str, None] = "b6ff49447f96"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
CREATE TABLE bar (
    id INT PRIMARY KEY,
    age INT NOT NULL,
);

charset latin1
"""
    )


def downgrade() -> None:
    op.execute("DROP TABLE bar;")
