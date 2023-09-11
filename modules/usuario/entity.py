from pydantic import BaseModel
from datetime import datetime


class UsuarioEntity(BaseModel):
    id: int | None
    nome_completo : str
    dt_nasc  : datetime
    email : str
    celular : str
    id_login: int
