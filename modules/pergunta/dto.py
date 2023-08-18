from pydantic import BaseModel

class PerguntaDTO(BaseModel):
    usuario: str
    titulo: str 
    pergunta: str
    
    
    