from pydantic import BaseModel
from typing import DateTime


class UsuarioDTO(BaseModel):
    id: int = None
    Nome_completo : str
    dt_nasc  : DateTime
    confirmacao_senha : str
    email : str
    celular : str
