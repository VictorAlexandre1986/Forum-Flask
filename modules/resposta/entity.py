from pydantic import BaseModel

class RespostaEntity(BaseModel):
    id: int 
    usuario: str
    resposta: str
    contagem_voto: int    