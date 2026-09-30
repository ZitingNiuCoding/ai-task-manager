"""create initial tables

Revision ID: 90c8198acf09
Revises: 
Create Date: 2026-09-30 23:01:44.695736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90c8198acf09'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # 先创建 users，因为 tasks 的外键依赖它
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            primary_key=True
        ),
        sa.Column("username", sa.Text(), nullable=False),
        sa.Column("email", sa.Text(), nullable=False),
        sa.Column("password_hash", sa.Text(), nullable=True),

        sa.UniqueConstraint(
            "username",
            name="users_username_unique"
        ),
        sa.UniqueConstraint(
            "email",
            name="users_email_unique"
        ),
    )

    # 再创建 tasks
    op.create_table(
        "tasks",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            primary_key=True
        ),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column(
            "completed",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false")
        ),
        sa.Column("user_id", sa.Integer(), nullable=True),

        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="tasks_user_id_fkey"
        ),
    )


def downgrade() -> None:
    op.drop_table("tasks")
    op.drop_table("users")

