from abc import ABC, abstractmethod

class LoginRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_login(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_logins(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_login_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_login(self, data: dict, id:int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_login(self, id: int):
        raise Exception("Método não implementado")