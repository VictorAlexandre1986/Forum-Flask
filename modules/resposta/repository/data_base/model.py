from sqlalchemy import Column, Integer,String, ForeignKey
from sqlalchemy.orm import relationship

from infra.db import Base
# from modules.login.repository.data_base.model import Login

class Resposta(Base):
    __tablename__ = "tb_resposta"
    
    resposta = Column(String, nullable=False)
    contagem_voto = Column(Integer, nullable=False)
    id_login = Column(Integer, ForeignKey("tb_login.id", ondelete="CASCADE", onupdate="CASCADE"))
    login = relationship('Login', back_populates='resposta')
    id_pergunta = Column(Integer, ForeignKey("tb_pergunta.id", ondelete="CASCADE", onupdate="CASCADE"))
    pergunta = relationship('Pergunta', back_populates='resposta')