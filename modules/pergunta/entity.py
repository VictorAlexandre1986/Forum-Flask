from pydantic import BaseModel

class PerguntaEntity(BaseModel):
    id:int
    id_login: int
    titulo: str 
    pergunta: str
    contagem_voto: int