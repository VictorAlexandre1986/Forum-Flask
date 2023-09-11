
class RespostaUseCase:
    
    def __init__(self, resposta_repository):
        self.resposta_repository = resposta_repository
        
    
    def criar_resposta(self, id: int, id_login: int, resposta: str, contagem_voto: int, id_pergunta: int):
        return self.resposta_repository.criar_resposta(id, id_login, resposta, contagem_voto, id_pergunta)
    
    def buscar_resposta_por_id(self, id: int):
        return self.resposta_repository.buscar_resposta_por_id(id)
    
    def buscar_respostas(self):
        return self.resposta_repository.buscar_respostas()
    
    def deletar_resposta(self, id: int):
        return self.resposta_repository.deletar_resposta(id)
    
    def atualizar_resposta(self, id: int, id_login: int, resposta: str, contagem_voto: int, id_pergunta: int):
        return self.resposta_repository.atualizar_resposta(id, id_login, resposta, contagem_voto, id_pergunta)

    def incrementar_pontuacao(self, id:int):
        return self.resposta_repository.incrementar_pontuacao(id)

    def decrementar_pontuacao(self, id: int):
        return self.resposta_repository.decrementar_pontuacao(id)