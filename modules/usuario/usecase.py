from datetime import datetime

class UsuarioUseCase:
    
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository
        
    
    def criar_usuario(self, id: int, nome_completo: str, dt_nasc: datetime, email:str, celular: str, id_login: int):
        return self.usuario_repository.criar_usuario(id, nome_completo, dt_nasc, email, celular, id_login)
    
    def buscar_usuario_por_id(self, id: int):
        return self.usuario_repository.buscar_usuario_por_id(id)
    
    def buscar_usuarios(self):
        return self.usuario_repository.buscar_usuarios()
    
    def deletar_usuario(self, id: int):
        return self.usuario_repository.deletar_usuario(id)
    
    def atualizar_usuario(self, id: int, nome_completo: str, dt_nasc: datetime, email:str, celular: str, id_login: int):
        return self.usuario_repository.atualizar_usuario(id, nome_completo, dt_nasc, email, celular, id_login)