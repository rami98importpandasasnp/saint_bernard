"""create adv table

Revision ID: 1230b6b4be3f
Revises: 
Create Date: 2024-02-24 12:17:30.038077

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "1230b6b4be3f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.execute("CREATE SCHEMA inventory;")
    op.create_table(
        "channel",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("platform", sa.Text, nullable=False),
        sa.Column("posts", sa.Integer, nullable=True),
        sa.Column("likes", sa.Integer, nullable=True),
        sa.Column("comments", sa.Integer, nullable=True),
        sa.Column("comments", sa.Integer, nullable=True),
        sa.Column("interactions", sa.Integer, nullable=True),
        sa.Column("reactions", sa.Integer, nullable=True),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_role")),
        schema="inventory",
    )
    op.create_table(
        "adv",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("category", sa.Text, nullable=True),
        sa.Column("sub_category", sa.Text, nullable=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("description", sa.Text, nullable=False),
        sa.Column("game_time", sa.Text, nullable=True),
        sa.Column("channel_ids", sa.ARRAY(sa.Integer()), nullable=True),
        sa.Column("duration", sa.Integer, nullable=True),
        sa.Column("visibility", sa.Integer, nullable=True),
        sa.Column("engagement", sa.Integer, nullable=True),
        sa.Column("grade", sa.Float, nullable=True),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_role")),
        sa.ForeignKeyConstraint(
            ["channel_ids"], ["channel.id"], name="fk_adv_channel_ids"
        ),
        schema="inventory",
    )

    op.create_table(
        "client",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.Integer, nullable=False),
        sa.Column("fiscale_code", sa.Integer, nullable=False),
        sa.Column("address", sa.Float, nullable=False),
        sa.Column("channel_ids", sa.ARRAY(sa.Integer()), nullable=True),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_role")),
        sa.ForeignKeyConstraint(
            ["channel_ids"], ["channel.id"], name="fk_client_channel_ids"
        ),
        schema="inventory",
    )

    op.create_table(
        "price",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("client_id", sa.Integer, nullable=False),
        sa.Column("grade", sa.Integer, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        schema="inventory",
    )


def downgrade() -> None:
    op.execute("DROP SCHEMA inventory;")
    op.drop_table("channel")
    op.drop_table("adv")
    op.drop_table("client")
    op.drop_table("price")
