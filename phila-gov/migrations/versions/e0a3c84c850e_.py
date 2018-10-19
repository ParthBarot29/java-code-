"""empty message

Revision ID: e0a3c84c850e
Revises: 
Create Date: 2018-10-19 13:58:52.247672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0a3c84c850e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer_information',
    sa.Column('brt_number', sa.String(length=80), nullable=False),
    sa.Column('property_address', sa.String(length=512), nullable=True),
    sa.Column('postal_code', sa.String(length=80), nullable=True),
    sa.Column('owner_name', sa.String(length=256), nullable=True),
    sa.Column('lien_sale_account', sa.String(length=5), nullable=True),
    sa.Column('payments_through', sa.String(length=20), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('brt_number')
    )
    op.create_table('real_estate_tax',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brt_number', sa.String(length=80), nullable=True),
    sa.Column('year', sa.String(length=5), nullable=True),
    sa.Column('principal', sa.Float(), nullable=True),
    sa.Column('interest', sa.Float(), nullable=True),
    sa.Column('penalty', sa.Float(), nullable=True),
    sa.Column('other_charges', sa.Float(), nullable=True),
    sa.Column('total_charges', sa.Float(), nullable=True),
    sa.Column('lien_number', sa.String(length=80), nullable=True),
    sa.Column('city_solicitor', sa.String(length=512), nullable=True),
    sa.Column('tax_status', sa.String(), nullable=True),
    sa.Column('currency', sa.String(length=5), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status_description',
    sa.Column('status_value', sa.String(length=10), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('status_value')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('status_description')
    op.drop_table('real_estate_tax')
    op.drop_table('customer_information')
    # ### end Alembic commands ###