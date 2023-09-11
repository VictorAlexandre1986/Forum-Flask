from pydantic import BaseModel



class UsuarioEntity(BaseModel):
    id: int = None
    Nome_completo : str
    dt_nasc  : str
    confirmacao_senha : str
    email : str
    celular : str
