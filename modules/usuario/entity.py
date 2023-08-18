from pydantic import BaseModel
from typing import Datetime


class UsuarioDTO(BaseModel):
    id: int = None
    Nome_completo : str
    dt_nasc  : Datetime
    confirmacao_senha : str
    email : str
    celular : str
