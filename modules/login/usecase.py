
class LoginUseCase:
    
    def ___init__(self, login_repository):
        self.login_repository = login_repository
        
    
    def criar_login(self, username: str, password: str):
        return self.login_repository.criar_login(username, password)
    
    def buscar_login(self, id: int):
        return self.login_repository.buscar_login(id)
    
    def buscar_login(self):
        return self.login_repository.buscar_login()
    
    def deletar_login(self, id: int):
        return self.login_repository.deletar_login(id)
    
    def atualizar_login(self, username:str, password:str):
        return self.login_repository.atualizar_login(username,password)