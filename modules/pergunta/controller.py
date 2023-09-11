from modules.pergunta.dto import PerguntaDTO
from modules.pergunta.repository.data_base.pergunta_repo import PerguntaRepository
from modules.pergunta.usecase import PerguntaUseCase



class PerguntaController:

    @staticmethod
    def criar_pergunta(data: dict):
        data_dto = PerguntaDTO(**data)
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).criar_pergunta(id = data_dto.id, id_login = data_dto.id_login, titulo= data_dto.titulo, pergunta= data_dto.pergunta, contagem_voto=data_dto.contagem_voto)
        return result
    
    @staticmethod
    def buscar_pergunta_por_id(id: int):
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).buscar_pergunta_por_id(id)
        return result
    
    @staticmethod
    def buscar_perguntas():
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).buscar_perguntas()
        result = [pergunta.dict() for pergunta in result]
        return result
    
    @staticmethod
    def atualizar_pergunta(data: dict, id: int):
        data_dto = PerguntaDTO(**data)
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).atualizar_pergunta(id=id, id_login = data_dto.id_login, titulo = data_dto.titulo, pergunta= data_dto.pergunta, contagem_voto= data_dto.contagem_voto)
        return result
    
    @staticmethod
    def deletar_pergunta(id: int):
        repository = PerguntaRepository()
        result = PerguntaUseCase(repository).deletar_pergunta(id)
        return result