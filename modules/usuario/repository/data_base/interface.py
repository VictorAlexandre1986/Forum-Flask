from abc import ABC, abstractmethod

class UsuarioRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_usuario(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_usuarios(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_usuario_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_usuario(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_usuario(self, id: int):
        raise Exception("Método não implementado")