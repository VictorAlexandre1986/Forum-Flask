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
            id_login=pergunta.id_login,
            titulo=pergunta.titulo,
            pergunta=pergunta.pergunta,
            contagem_voto=pergunta.contagem_voto
        )

    def criar_pergunta(self, id: int, id_login: int, titulo: str, pergunta: str, contagem_voto: int):
        try:
            with DBConnectionHandler() as db_connection:
                nova_pergunta = Pergunta( id=id, id_login=id_login, titulo=titulo,pergunta=pergunta ,contagem_voto=contagem_voto)
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
        
    def atualizar_pergunta(self, id: int, id_login: int, titulo: str, pergunta: str, contagem_voto: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Pergunta).filter(Pergunta.id == id).one_or_none()
            if data:
                id=id
                data.id_login = id_login
                data.titulo = titulo
                data.pergunta = pergunta
                data.contagem_voto = contagem_voto
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