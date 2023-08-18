from pydantic import BaseModel

class PerguntaEntity(BaseModel):
    usuario: str
    titulo: str 
    pergunta: str
    contagem_voto: int