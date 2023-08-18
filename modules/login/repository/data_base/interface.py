from abc import ABC, abstractmethod

class LoginRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_login(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_login(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_login_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_login(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_login(self, id: int):
        raise Exception("Método não implementado")