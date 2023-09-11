from pydantic import BaseModel



class UsuarioDTO(BaseModel):
    id: int = None
    Nome_completo : str
    dt_nasc  : str
    email : str
    celular : str
