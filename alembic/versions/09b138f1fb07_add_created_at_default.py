"""add created at default

Revision ID: 09b138f1fb07
Revises: 2140da050245
Create Date: 2026-09-17 23:24:26.633004

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "09b138f1fb07"
down_revision: Union[str, Sequence[str], None] = "2140da050245"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "procurement_requests",
        "created_at",
        server_default=sa.text("now()"),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "procurement_requests",
        "created_at",
        server_default=None,
        existing_nullable=False,
    )
