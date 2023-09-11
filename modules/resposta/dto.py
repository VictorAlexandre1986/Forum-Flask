from pydantic import BaseModel

class RespostaDTO(BaseModel):
    id: int
    id_login: int
    resposta: str
    contagem_voto: int    
    id_pergunta:int
    
