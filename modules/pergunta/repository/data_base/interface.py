from abc import ABC, abstractmethod

class PerguntaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_pergunta(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_perguntas(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_pergunta_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_pergunta(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_pergunta(self, id: int):
        raise Exception("Método não implementado")