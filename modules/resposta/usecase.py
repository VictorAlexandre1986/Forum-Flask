
class RespostaUseCase:
    
    def ___init__(self, resposta_repository):
        self.resposta_repository = resposta_repository
        
    
    def criar_resposta(self, username: str, resposta: str):
        return self.resposta_repository.criar_resposta(username, resposta)
    
    def buscar_resposta(self, id: int):
        return self.resposta_repository.buscar_resposta(id)
    
    def buscar_respostas(self):
        return self.resposta_repository.buscar_respostas()
    
    def deletar_resposta(self, id: int):
        return self.resposta_repository.deletar_resposta(id)
    
    def atualizar_resposta(self, username:str, resposta:str):
        return self.resposta_repository.atualizar_resposta(username, resposta)