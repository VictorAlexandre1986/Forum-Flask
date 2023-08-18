from modules.resposta.dto import RespostaDTO
from modules.resposta.repository.data_base.resposta_repo import RespostaRepository
from modules.resposta.usecase import RespostaUseCase



class RespostaController:

    @staticmethod
    def criar_resposta(data: dict):
        data_dto = RespostaDTO(**data)
        repository = RespostaRepository()
        result = RespostaUseCase(repository).criar_resposta(id = data_dto.id, id_usuario = data_dto.id_usuario, resposta = data_dto.resposta, contagem_voto= data_dto.contagem_voto)
        return result
    
    @staticmethod
    def buscar_resposta_por_id(id: int):
        repository = RespostaRepository()
        result = RespostaUseCase(repository).buscar_resposta_por_id(id)
        return result
    
    @staticmethod
    def buscar_repostas():
        repository = RespostaRepository()
        result = RespostaUseCase(repository).buscar_repostas()
        result = [resposta.dict() for resposta in result]
        return result
    
    @staticmethod
    def atualizar_resposta(data: dict, id: int):
        data_dto = RespostaDTO(**data)
        # id_usuario= data_dto.id_usuario
        # resposta = data_dto.resposta
        # contagem_voto = data_dto.contagem_voto   
        repository = RespostaRepository()
        result = RespostaUseCase(repository).atualizar_resposta(id=id, id_usuario = data_dto.id_usuario, resposta = data_dto.resposta, contagem_voto= data_dto.contagem_voto)
        return result

    @staticmethod
    def incrementar_pontuacao(id: int):
        repository = RespostaRepository()
        result = RespostaUseCase(repository).incrementar_pontuacao(id=id)
        return result

    @staticmethod
    def decrementar_pontuacao(id: int):
        repository = RespostaRepository()
        result = RespostaUseCase(repository).decrementar_pontuacao(id=id)
        return result
    
    @staticmethod
    def deletar_resposta(id: int):
        repository = RespostaRepository()
        result = RespostaUseCase(repository).deletar_resposta(id)
        return result