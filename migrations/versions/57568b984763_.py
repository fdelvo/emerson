"""empty message

Revision ID: 57568b984763
Revises: 7218d0268966
Create Date: 2017-08-14 18:21:32.565896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57568b984763'
down_revision = '7218d0268966'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('embedded_link', sa.String(length=256), nullable=False))
    op.drop_constraint('video_embeded_link_key', 'video', type_='unique')
    op.create_unique_constraint(None, 'video', ['embedded_link'])
    op.drop_column('video', 'embeded_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('embeded_link', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'video', type_='unique')
    op.create_unique_constraint('video_embeded_link_key', 'video', ['embeded_link'])
    op.drop_column('video', 'embedded_link')
    # ### end Alembic commands ###