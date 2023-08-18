from infra.db.db_config import DBConnectionHandler
from modules.pergunta.repository.data_base.interface import PerguntaRepositoryInterface
from modules.pergunta.repository.data_base.model import Pergunta
from modules.pergunta.entity import PerguntaEntity
from datetime import datetime
import uuid as uuid


class PerguntaRepository(PerguntaRepositoryInterface):

    def _criar_pergunta_objeto(self, pergunta):
        return PerguntaEntity(
            id=pergunta.id,
            uuid=pergunta.uuid,
            usuario=pergunta.id_usuario,
            pergunta=pergunta.pergunta,
        )

    def criar_pergunta(self, uuid: uuid, id_usuario: int, pergunta: str):
        try:
            with DBConnectionHandler() as db_connection:
                nova_pergunta = Pergunta( uuid=uuid, usuario=id_usuario, pergunta=pergunta)
                db_connection.session.add(nova_pergunta)
                db_connection.session.commit()
                return self._criar_pergunta_objeto(nova_pergunta)
        except Exception as exc:
            raise exc

    def buscar_pergunta_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Pergunta).filter(Pergunta.id == id).one_or_none()
            data_resultado = self._criar_pergunta_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_perguntas(self):
        with DBConnectionHandler() as db_connection:
            list_perguntas = []
            perguntas = db_connection.session.query(Pergunta).all()
            for pergunta in perguntas:
                list_perguntas.append(
                    self._criar_pergunta_objeto(pergunta)
                )
            return list_perguntas
        
    def atualizar_pergunta(self, id: int, id_usuario: int, pergunta: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Pergunta).filter(Pergunta.id == id).one_or_none()
            if data:
                data.id_usuario = id_usuario
                data.pergunta = pergunta
                db_connection.session.commit()
                return self._criar_pergunta_objeto(data)
            return None

    def deletar_pergunta(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Pergunta).filter(Pergunta.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_pergunta_objeto(data)
            return data