"""Création de la table des produits manquants

Revision ID: b87b892e4bc3
Revises:
Create Date: 2018-08-07 22:07:41.089556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b87b892e4bc3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'produits_manquants',
        sa.Column('nom', sa.String(128), primary_key=True),
    )


def downgrade():
    op.drop_table('produits_manquants')
