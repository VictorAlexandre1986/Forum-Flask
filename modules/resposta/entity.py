from pydantic import BaseModel

class RespostaEntity(BaseModel):
    id: int
    id_login: int
    resposta: str
    contagem_voto: int    
    id_pergunta:int