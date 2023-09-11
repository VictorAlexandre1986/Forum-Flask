from abc import ABC, abstractmethod

class RespostaRepositoryInterface(ABC):
    
    @abstractmethod
    def criar_resposta(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod 
    def buscar_respostas(self):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def buscar_resposta_por_id(self, id: int):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def atualizar_resposta(self, data: dict):
        raise Exception("Método não implementado")
    
    @abstractmethod
    def deletar_resposta(self, id: int):
        raise Exception("Método não implementado")

    @abstractmethod
    def incrementar_pontuacao(self, id: int):
        raise Exception("Método não implementado")

    @abstractmethod
    def decrementar_pontuacao(self, id: int):
        raise Exception("Método não implementado")