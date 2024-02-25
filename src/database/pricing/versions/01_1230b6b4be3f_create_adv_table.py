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

    op.execute("CREATE SCHEMA price;")
    op.create_table(
        "client",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("fiscale_code", sa.Text, nullable=False),
        sa.Column("address", sa.Text, nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_client")),
        schema="price",
    )
    op.create_table(
        "platform",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.Text),
        schema="price",
    )

    op.create_table(
        "channel",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("client_id", sa.Integer, nullable=False),
        sa.Column("platform_id", sa.Integer, nullable=False),
        sa.Column("posts", sa.Integer, nullable=True),
        sa.Column("likes", sa.Integer, nullable=True),
        sa.Column("comments", sa.Integer, nullable=True),
        sa.Column("interactions", sa.Integer, nullable=True),
        sa.Column("reactions", sa.Integer, nullable=True),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_channel")),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["price.client.id"],
            name="fk_channel_client_ids",
            on_update="CASCADE",
            on_delete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["platform_id"],
            ["price.platform.id"],
            name="fk_channel_platform_ids",
            on_update="CASCADE",
            on_delete="CASCADE",
        ),
        schema="price",
    )
    op.create_table(
        "adv",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("category", sa.Text, nullable=True),
        sa.Column("sub_category", sa.Text, nullable=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("description", sa.Text, nullable=False),
        sa.Column("game_time", sa.Text, nullable=True),
        sa.Column("platform_id", sa.Integer, nullable=True),
        sa.Column("duration", sa.Integer, nullable=True),
        sa.Column("visibility", sa.Integer, nullable=True),
        sa.Column("engagement", sa.Integer, nullable=True),
        sa.Column("grade", sa.Float, nullable=True),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_adv")),
        sa.ForeignKeyConstraint(
            ["platform_id"],
            ["price.platform.id"],
            name="fk_adv_platform_ids",
            on_update="CASCADE",
            on_delete="CASCADE",
        ),
        schema="price",
    )

    op.create_table(
        "sale",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("client_id", sa.Integer, nullable=False),
        sa.Column("adv_id", sa.Integer, nullable=False),
        sa.Column("amount", sa.Integer, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_sale")),
        sa.ForeignKeyConstraint(
            ["adv_id"],
            ["price.adv.id"],
            name="fk_sale_adv_ids",
            on_update="CASCADE",
            on_delete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["price.client.id"],
            name="fk_sale_client_ids",
            on_update="CASCADE",
            on_delete="CASCADE",
        ),
        schema="price",
    )

    op.create_table(
        "inventory",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("adv_id", sa.Integer, nullable=False),
        sa.Column("client_id", sa.Integer, nullable=False),
        sa.Column("grade", sa.Integer, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column(
            "created_at", sa.DateTime, nullable=False, server_default=sa.func.now()
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_inventory")),
        sa.ForeignKeyConstraint(
            ["adv_id"],
            ["price.adv.id"],
            name="fk_inventory_adv_ids",
            on_update="CASCADE",
            on_delete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["price.client.id"],
            name="fk_inventory_client_ids",
            on_update="CASCADE",
            on_delete="CASCADE",
        ),
        schema="price",
    )


def downgrade() -> None:
    op.drop_constraint(
        constraint_name="fk_channel_client_ids",
        table_name="channel",
        schema="price",
        type_="foreignkey",
    )
    op.drop_constraint(
        constraint_name="fk_channel_platform_ids",
        table_name="channel",
        schema="price",
        type_="foreignkey",
    )
    op.drop_constraint(
        constraint_name="fk_adv_platform_ids",
        table_name="adv",
        schema="price",
        type_="foreignkey",
    )
    op.drop_constraint(
        constraint_name="fk_sale_adv_ids",
        table_name="sale",
        schema="price",
        type_="foreignkey",
    )
    op.drop_constraint(
        constraint_name="fk_sale_client_ids",
        table_name="sale",
        schema="price",
        type_="foreignkey",
    )
    op.drop_constraint(
        constraint_name="fk_inventory_adv_ids",
        table_name="inventory",
        schema="price",
        type_="foreignkey",
    )
    op.drop_constraint(
        constraint_name="fk_inventory_client_ids",
        table_name="inventory",
        schema="price",
        type_="foreignkey",
    )

    op.drop_table("client", schema="price")
    op.drop_table("platform", schema="price")
    op.drop_table("channel", schema="price")
    op.drop_table("adv", schema="price")
    op.drop_table("sale", schema="price")
    op.drop_table("inventory", schema="price")

    op.execute("DROP SCHEMA price cascade;")
