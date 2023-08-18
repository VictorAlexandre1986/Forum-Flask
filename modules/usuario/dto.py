from pydantic import BaseModel
from typing import Datetime


class UsuarioDTO(BaseModel):
    id: int = None
    Nome_completo : str
    dt_nasc  : Datetime
    email : str
    celular : str
