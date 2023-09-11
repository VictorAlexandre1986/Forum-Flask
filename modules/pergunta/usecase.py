
class PerguntaUseCase:
    
    def __init__(self, pergunta_repository):
        self.pergunta_repository = pergunta_repository
        
    
    def criar_pergunta(self, id:int, id_login: int, titulo: str ,pergunta: str, contagem_voto: int):
        return self.pergunta_repository.criar_pergunta(id, id_login, titulo, pergunta, contagem_voto)
    
    def buscar_pergunta_por_id(self, id: int):
        return self.pergunta_repository.buscar_pergunta_por_id(id)
    
    def buscar_perguntas(self):
        return self.pergunta_repository.buscar_perguntas()
    
    def deletar_pergunta(self, id: int):
        return self.pergunta_repository.deletar_pergunta(id)
    
    def atualizar_pergunta(self, id: int, id_login: int, titulo: str, pergunta:str, contagem_voto: int):
        return self.pergunta_repository.atualizar_pergunta(id, id_login, titulo, pergunta, contagem_voto)