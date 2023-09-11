from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from usuario.repository.data_base.model import Usuario

from infra.db import Base

class Login(Base):
    __tablename__ = "tb_login"
    
    id = Column(Integer,  primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    usuario = relationship(Usuario, backref="login", cascade='all, delete')