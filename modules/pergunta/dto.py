from pydantic import BaseModel

class PerguntaDTO(BaseModel):
    id:int
    id_login: int
    titulo: str 
    pergunta: str
    contagem_voto: int
    
    
    