from sqlalchemy import Column, Integer,String, DateTime,ForeignKey
from sqlalchemy.orm import relationship
# from modules.login.repository.data_base.model import Login

from infra.db import Base

class Usuario(Base):
    __tablename__ = "tb_usuario"
    
    id = Column(Integer, primary_key=True)
    nome_completo = Column(String, nullable=False)
    dt_nasc = Column(DateTime, nullable=False)
    email = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    id_login = Column(Integer, ForeignKey('tb_login.id', ondelete="CASCADE", onupdate="CASCADE"))
    login = relationship('Login', back_populates='usuario')