from pydantic import BaseModel

class RespostaDTO(BaseModel):
    id: int
    id_usuario: int
    resposta: str
    contagem_voto: int    