
class PerguntaUseCase:
    
    def ___init__(self, pergunta_repository):
        self.pergunta_repository = pergunta_repository
        
    
    def criar_pergunta(self, username: str, titulo: str ,pergunta: str):
        return self.pergunta_repository.criar_pergunta(username, titulo, pergunta)
    
    def buscar_pergunta(self, titulo: str):
        return self.pergunta_repository.buscar_pergunta(titulo)
    
    def buscar_perguntas(self):
        return self.pergunta_repository.buscar_perguntas()
    
    def deletar_pergunta(self, id: int):
        return self.pergunta_repository.deletar_pergunta(id)
    
    def atualizar_pergunta(self, titulo:str, pergunta:str):
        return self.usuario_repository.atualizar_usuario(titulo, pergunta)