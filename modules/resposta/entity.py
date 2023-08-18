from pydantic import BaseModel

class RespostaEntity(BaseModel):
    id: int 
    id_usuario: int
    resposta: str
    contagem_voto: int    