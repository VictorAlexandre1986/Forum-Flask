from pydantic import BaseModel

class PerguntaEntity(BaseModel):
    id:int
    usuario: str
    titulo: str 
    pergunta: str
    contagem_voto: int