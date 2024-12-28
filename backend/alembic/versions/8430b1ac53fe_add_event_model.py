"""Add event model

Revision ID: 8430b1ac53fe
Revises: 615c51060ea1
Create Date: 2024-12-19 22:11:13.394387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8430b1ac53fe'
down_revision: Union[str, None] = '615c51060ea1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('max_participants', sa.Integer(), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('contact_email', sa.String(length=255), nullable=True),
    sa.Column('contact_phone_code', sa.String(length=12), nullable=True, comment='Phone number with country code, e.g. +47'),
    sa.Column('contact_phone_number', sa.String(length=32), nullable=True, comment='Phone number with country code, e.g. 99887766'),
    sa.Column('maps_url', sa.String(length=255), nullable=True),
    sa.Column('address_street', sa.String(length=255), nullable=True),
    sa.Column('address_city', sa.String(length=255), nullable=True),
    sa.Column('address_postal_code', sa.String(length=50), nullable=True),
    sa.Column('address_country', sa.String(length=255), nullable=True),
    sa.Column('start_at', sa.DateTime(), nullable=False),
    sa.Column('end_at', sa.DateTime(), nullable=False),
    sa.Column('organisation_id', sa.UUID(), nullable=False),
    sa.Column('created_by_id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_events_title'), 'events', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_events_title'), table_name='events')
    op.drop_table('events')
    # ### end Alembic commands ###
