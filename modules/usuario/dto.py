from pydantic import BaseModel



class UsuarioDTO(BaseModel):
    id: int | None
    nome_completo : str
    dt_nasc  : str | None
    email : str
    celular : str
    id_login: int
