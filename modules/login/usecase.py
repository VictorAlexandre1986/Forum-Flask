
class LoginUseCase:
    
    def __init__(self, login_repository):
        self.login_repository = login_repository
        
    
    def criar_login(self, id:int, username: str, password: str):
        return self.login_repository.criar_login(id,username, password)
    
    def buscar_login_por_id(self, id: int):
        return self.login_repository.buscar_login_por_id(id)
    
    def buscar_logins(self):
        return self.login_repository.buscar_logins()
    
    def deletar_login(self, id: int):
        return self.login_repository.deletar_login(id)
    
    def atualizar_login(self,id:int, username:str, password:str):
        return self.login_repository.atualizar_login(id, username, password)