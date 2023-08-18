from abc import ABC, abstractmethod

class RespostaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_resposta(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_respostas(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_reposta_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_resposta(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_resposta(self, id: int):
        raise Exception("Método não implementado")