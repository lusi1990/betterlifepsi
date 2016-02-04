# coding=utf-8
"""增加某产品是否需要运营建议的选项

Revision ID: faa0a5506a14
Revises: 38571f2c12fc
Create Date: 2016-02-04 15:55:19.050763

"""

# revision identifiers, used by Alembic.
revision = 'faa0a5506a14'
down_revision = '38571f2c12fc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('need_advice', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'need_advice')
    ### end Alembic commands ###
