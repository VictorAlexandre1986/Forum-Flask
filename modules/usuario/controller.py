from modules.usuario.dto import UsuarioDTO
from modules.usuario.repository.data_base.usuario_repo import UsuarioRepository
from modules.usuario.usecase import UsuarioUseCase
from datetime import datetime


class UsuarioController:

    @staticmethod
    def criar_usuario(data: dict):
        data_dto = UsuarioDTO(**data)
        repository = UsuarioRepository()
        dt_nasc =  datetime.strptime(data_dto.dt_nasc, '%Y-%m-%d')
        result = UsuarioUseCase(repository).criar_usuario(id= data_dto.id, nome_completo = data_dto.nome_completo, dt_nasc = dt_nasc, email= data_dto.email, celular= data_dto.celular, id_login=data_dto.id_login)
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
        list_usuarios = []
        for indice,valor in enumerate(result):
            id = result[indice]["id"]
            nome_completo = result[indice]["nome_completo"]
            dt_nasc = result[indice]["dt_nasc"]
            email = result[indice]["email"]
            celular = result[indice]["celular"]
            id_login = result[indice]["id_login"]

            data_formatada = dt_nasc.strftime("%d/%m/%Y %H:%M:%S")

            usuario={}
            usuario.update({"id":id, "nome_completo":nome_completo, "dt_nasc":data_formatada ,"email":email, "celular":celular, "id_login":id_login})
            list_usuarios.append(usuario)
        return list_usuarios
        
    
    @staticmethod
    def atualizar_usuario(data: dict, id: int):
        data_dto = UsuarioDTO(**data)
        dt_nasc = data_dto.dt_nasc
        date_nasc = datetime.strptime(data_dto.dt_nasc, '%Y-%m-%d')
        repository = UsuarioRepository()
        result = UsuarioUseCase(repository).atualizar_usuario(id=id, nome_completo = data_dto.nome_completo, dt_nasc = date_nasc, email= data_dto.email, celular= data_dto.celular, id_login = data_dto.id_login)
        return result
    
    @staticmethod
    def deletar_usuario(id: int):
        repository = UsuarioRepository()
        result = UsuarioUseCase(repository).deletar_usuario(id)
        return result