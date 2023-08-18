from modules.pergunta.dto import PerguntaDTO
from modules.pergunta.repository.data_base.pergunta_repo import PerguntaRepository
from modules.pergunta.usecase import PerguntaUseCase



class PerguntaController:

    @staticmethod
    def criar_pergunta(data: dict):
        data_dto = PerguntaDTO(**data)
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).criar_pergunta(dt_validity = data_dto.dt_validity, vl_tax = data_dto.vl_tax, st_active= data_dto.st_active, id_coin= data_dto.id_coin)
        return result
    
    @staticmethod
    def buscar_pergunta_por_id(id: int):
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).buscar_pergunta_por_id(id)
        return result
    
    @staticmethod
    def buscar_changes():
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).buscar_changes()
        result = [change.dict() for change in result]
        return result
    
    @staticmethod
    def atualizar_pergunta(data: dict, id: int):
        data_dto = PerguntaDTO(**data)
        dt_validity= data_dto.dt_validity
        date_validity = dt_validity.strftime("%Y-%m-%d %H:%M:%S")
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).atualizar_pergunta(id=id, dt_validity = date_validity, vl_tax = data_dto.vl_tax, st_active= data_dto.st_active, id_coin= data_dto.id_coin)
        return result
    
    @staticmethod
    def deletar_pergunta(id: int):
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).deletar_pergunta(id)
        return result