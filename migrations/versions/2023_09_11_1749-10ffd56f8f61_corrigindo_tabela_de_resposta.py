"""corrigindo tabela de resposta

Revision ID: 10ffd56f8f61
Revises: 
Create Date: 2023-09-11 17:49:08.366482

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10ffd56f8f61'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_login',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date_create', sa.DateTime(timezone=True), nullable=False),
    sa.Column('update_create', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_pergunta',
    sa.Column('titulo', sa.String(), nullable=False),
    sa.Column('pergunta', sa.String(), nullable=False),
    sa.Column('contagem_voto', sa.Integer(), nullable=False),
    sa.Column('id_login', sa.Integer(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date_create', sa.DateTime(timezone=True), nullable=False),
    sa.Column('update_create', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['id_login'], ['tb_login.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_completo', sa.String(), nullable=False),
    sa.Column('dt_nasc', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('celular', sa.String(), nullable=False),
    sa.Column('id_login', sa.Integer(), nullable=True),
    sa.Column('date_create', sa.DateTime(timezone=True), nullable=False),
    sa.Column('update_create', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['id_login'], ['tb_login.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_resposta',
    sa.Column('resposta', sa.String(), nullable=False),
    sa.Column('contagem_voto', sa.Integer(), nullable=False),
    sa.Column('id_login', sa.Integer(), nullable=True),
    sa.Column('id_pergunta', sa.Integer(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date_create', sa.DateTime(timezone=True), nullable=False),
    sa.Column('update_create', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['id_login'], ['tb_login.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_pergunta'], ['tb_pergunta.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_resposta')
    op.drop_table('tb_usuario')
    op.drop_table('tb_pergunta')
    op.drop_table('tb_login')
    # ### end Alembic commands ###
