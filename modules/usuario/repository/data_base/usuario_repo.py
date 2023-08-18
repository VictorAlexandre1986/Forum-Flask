from infra.db.db_config import DBConnectionHandler
from modules.usuario.repository.data_base.interface import UsuarioRepositoryInterface
from modules.usuario.repository.data_base.model import Usuario
from modules.usuario.entity import UsuarioEntity
from datetime import datetime
import uuid as uuid


class UsuarioRepository(UsuarioRepositoryInterface):

    def _criar_usuario_objeto(self, usuario):
        return UsuarioEntity(
            id=usuario.id,
            uuid=usuario.uuid,
            nome_completo=usuario.nome_completo,
            dt_nasc=usuario.dt_nasc,
            email = usuario.email,
            celular = usuario.celular,
        )

    def criar_usuario(self, uuid: uuid, nome_completo: str, dt_nasc: datetime, email: str, celular: str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_usuario = Usuario( uuid=uuid, nome_completo=nome_completo, dt_nasc=dt_nasc, email=email, celular=celular)
                db_connection.session.add(novo_usuario)
                db_connection.session.commit()
                return self._criar_usuario_objeto(novo_usuario)
        except Exception as exc:
            raise exc

    def buscar_pergunta_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Usuario).filter(Usuario.id == id).one_or_none()
            data_resultado = self._criar_usuario_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_usuarios(self):
        with DBConnectionHandler() as db_connection:
            list_usuarios = []
            usuarios = db_connection.session.query(Usuario).all()
            for usuario in usuarios:
                list_usuarios.append(
                    self._criar_usuario_objeto(usuario)
                )
            return list_usuarios
        
    def atualizar_usuario(self, id: int, nome_completo: str, dt_nasc: datetime, email: str, celular: str ):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Usuario).filter(Usuario.id == id).one_or_none()
            if data:
                data.nome_completo = nome_completo
                data.dt_nasc = dt_nasc
                data.email = email
                data.celular = celular 
                db_connection.session.commit()
                return self._criar_usuario_objeto(data)
            return None

    def deletar_usuario(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Usuario).filter(Usuario.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_usuario_objeto(data)
            return data