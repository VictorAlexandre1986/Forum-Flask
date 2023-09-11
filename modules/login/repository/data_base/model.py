from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from modules.usuario.repository.data_base.model import Usuario
from modules.resposta.repository.data_base.model import Resposta
from modules.pergunta.repository.data_base.model import Pergunta

from infra.db import Base

class Login(Base):
    __tablename__ = "tb_login"
    
    
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    usuario = relationship(Usuario, back_populates='login')
    resposta = relationship(Resposta, back_populates='login')
    pergunta = relationship(Pergunta, back_populates='login')