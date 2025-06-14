"""empty message

Revision ID: 803061fedd2d
Revises: 551fc74f4e73
Create Date: 2025-05-30 16:09:45.280184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '803061fedd2d'
down_revision = '551fc74f4e73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.alter_column('borrower_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('loan_start_date',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.alter_column('loan_end_date',
               existing_type=sa.DATE(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('loans', schema=None) as batch_op:
        batch_op.alter_column('loan_end_date',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.alter_column('loan_start_date',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.alter_column('borrower_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
