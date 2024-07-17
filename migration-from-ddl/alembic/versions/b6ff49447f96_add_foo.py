"""Add foo

Revision ID: b6ff49447f96
Revises:
Create Date: 2024-07-17 02:11:59.521410

"""

from typing import Sequence
from typing import Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "b6ff49447f96"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
CREATE TABLE foo (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
);

charset latin1
"""
    )


def downgrade() -> None:
    op.execute("DROP TABLE foo;")
