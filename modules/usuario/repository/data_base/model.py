from sqlalchemy import Column, Integer,String, Datetime
from sqlalchemy.orm import relationship

from infra.db import Base
from modules.usuario.repository.data_base.model import Usuario

class Usuario(Base):
    __tablename__ = "tb_usuario"
    
    nome_completo = Column(String, nullable=False)
    dt_nasc = Column(Datetime, nullable=False)
    email = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    pontuacao = Column(Integer, nullable=False)