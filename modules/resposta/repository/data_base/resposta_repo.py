from infra.db.db_config import DBConnectionHandler
from modules.resposta.repository.data_base.interface import RespostaRepositoryInterface
from modules.resposta.repository.data_base.model import Resposta
from modules.resposta.entity import RespostaEntity
from datetime import datetime
import uuid as uuid


class RespostaRepository(RespostaRepositoryInterface):

    def _criar_resposta_objeto(self, resposta):
        return RespostaEntity(
            id=resposta.id,
            uuid=resposta.uuid,
            id_usuario=resposta.id_usuario,
            resposta=resposta.resposta,
        )

    def criar_resposta(self, uuid: uuid, id_usuario: int, resposta: str, contagem_voto: int):
        try:
            with DBConnectionHandler() as db_connection:
                nova_resposta = Resposta( uuid=uuid, id_usuario=id_usuario, resposta=resposta, contagem_voto=contagem_voto)
                db_connection.session.add(nova_resposta)
                db_connection.session.commit()
                return self._criar_resposta_objeto(nova_resposta)
        except Exception as exc:
            raise exc

    def buscar_reposta_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Resposta).filter(Resposta.id == id).one_or_none()
            data_resultado = self._criar_resposta_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_respostas(self):
        with DBConnectionHandler() as db_connection:
            list_respostas = []
            respostas = db_connection.session.query(Resposta).all()
            for resposta in respostas:
                list_respostas.append(
                    self._criar_resposta_objeto(resposta)
                )
            return list_respostas
        
    def atualizar_resposta(self, id: int, id_usuario: int, resposta: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Resposta).filter(Resposta.id == id).one_or_none()
            if data:
                data.id_usuario = id_usuario
                data.resposta = resposta
                db_connection.session.commit()
                return self._criar_pergunta_objeto(data)
            return None

    def deletar_resposta(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Resposta).filter(Resposta.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_resposta_objeto(data)
            return data
        
        
    def incrementar_pontuacao(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Resposta).filter(Resposta.id == id).one_or_none()
            if data:
                if data.contagem_voto != 0:
                    data.contagem_voto = (data.contagem_voto + 1)
                    db_connection.session.commit()
                    return self._criar_pergunta_objeto(data)
            return None
        
    def decrementar_pontuacao(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Resposta).filter(Resposta.id == id).one_or_none()
            if data:
                if data.contagem_voto != 0:
                    data.contagem_voto = int(data.contagem_voto - 1)
                    db_connection.session.commit()
                    return self._criar_pergunta_objeto(data)
                else:
                    raise ValueError('Você não tem votos para remover')
            return None