"""fix procurement request timestamp

Revision ID: 2140da050245
Revises: 80a9866ef0aa
Create Date: 2026-09-17 23:17:04.200652

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "2140da050245"
down_revision: Union[str, Sequence[str], None] = "80a9866ef0aa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "procurement_requests",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        server_default=sa.text("now()"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.alter_column(
        "procurement_requests",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
        server_default=None,
    )
    # ### end Alembic commands ###
