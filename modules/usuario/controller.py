from modules.usuario.dto import UsuarioDTO
from modules.usuario.repository.data_base.usuario_repo import UsuarioRepository
from modules.usuario.usecase import UsuarioUseCase



class UsuarioController:

    @staticmethod
    def criar_usuario(data: dict):
        data_dto = UsuarioDTO(**data)
        repository = UsuarioRepository()
        result = UsuarioUseCase(repository).criar_usuario(nome_completo = data_dto.nome_completo, dt_nasc = data_dto.dt_nasc, email= data_dto.email, celular= data_dto.celular)
        return result
    
    @staticmethod
    def buscar_usuario_por_id(id: int):
        repository = UsuarioRepository()
        result = UsuarioUseCase(repository).buscar_usuario_por_id(id)
        return result
    
    @staticmethod
    def buscar_usuarios():
        repository = UsuarioRepository()
        result = UsuarioUseCase(repository).buscar_usuarios()
        result = [change.dict() for change in result]
        return result
    
    @staticmethod
    def atualizar_usuario(data: dict, id: int):
        data_dto = UsuarioDTO(**data)
        repository = UsuarioRepository()
        result = UsuarioUseCase(repository).atualizar_usuario(nome_completo = data_dto.nome_completo, dt_nasc = data_dto.dt_nasc, email= data_dto.email, celular= data_dto.celular)
        return result
    
    @staticmethod
    def deletar_pergunta(id: int):
        repository = UsuarioRepository()
        result = UsuarioUseCase(repository).deletar_usuario(id)
        return result