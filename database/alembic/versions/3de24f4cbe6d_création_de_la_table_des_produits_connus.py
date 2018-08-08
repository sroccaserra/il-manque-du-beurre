"""Création de la table des produits connus

Revision ID: 3de24f4cbe6d
Revises: b87b892e4bc3
Create Date: 2018-08-08 08:28:27.757088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3de24f4cbe6d'
down_revision = 'b87b892e4bc3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'produits_connus',
        sa.Column('nom', sa.String(128), primary_key=True),
    )
    bind = op.get_bind()
    bind.execute("INSERT INTO produits_connus(nom) VALUES "
                 "('beurre'), "
                 "('lessive'),"
                 "('dentifrice enfants')")

def downgrade():
    op.drop_table('produits_connus')
