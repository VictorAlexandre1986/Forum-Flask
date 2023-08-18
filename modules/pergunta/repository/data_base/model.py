from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship

from infra.db import Base
from modules.usuario.repository.data_base.model import Usuario

class Pergunta(Base):
    __tablename__ = "tb_pergunta"
    
    pergunta = Column(str, nullable=False)
    id_usuario = Column(Integer, ForeignKey("tb_usuario.id"))
    usuario = relationship(Usuario, lazy="joined")