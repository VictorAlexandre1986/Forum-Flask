
class UsuarioUseCase:
    
    def ___init__(self, usuario_repository):
        self.usuario_repository = usuario_repository
        
    
    def criar_usuario(self, data: dict):
        return self.usuario_repository.criar_usuario(data)
    
    def buscar_usuario(self, id: int):
        return self.usuario_repository.buscar_usuario(id)
    
    def buscar_usuarios(self):
        return self.usuario_repository.buscar_usuarios()
    
    def deletar_usuario(self, id: int):
        return self.usuario_repository.deletar_usuario(id)
    
    def atualizar_usuario(self, data: dict):
        return self.usuario_repository.atualizar_usuario(data)