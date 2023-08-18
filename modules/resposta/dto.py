from pydantic import BaseModel

class RespostaDTO(BaseModel):
    usuario: str
    resposta: str
    contagem_voto: int    