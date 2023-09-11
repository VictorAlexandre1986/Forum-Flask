from infra.db.db_config import DBConnectionHandler
from modules.login.repository.data_base.interface import LoginRepositoryInterface
from modules.login.repository.data_base.model import Login
from modules.login.dto import LoginDTO
from datetime import datetime
import uuid as uuid


class LoginRepository(LoginRepositoryInterface):

    def _criar_login_objeto(self, login):
        return LoginDTO(
            id=login.id,
            # uuid=login.uuid,
            username=login.username,
            password=login.password,
        )

    def criar_login(self, id: int, username: str, password:str):
        try:
            with DBConnectionHandler() as db_connection:
                novo_login = Login(id=id, username=username, password=password)
                db_connection.session.add(novo_login)
                db_connection.session.commit()
                print(self._criar_login_objeto(novo_login))
                return self._criar_login_objeto(novo_login)
        except Exception as exc:
            raise exc

    def buscar_login_por_id(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Login).filter(Login.id == id).one_or_none()
            data_resultado = self._criar_login_objeto(data)
            if data_resultado is not None:
                return data_resultado

    def buscar_logins(self):
        with DBConnectionHandler() as db_connection:
            list_logins = []
            logins = db_connection.session.query(Login).all()
            for login in logins:
                list_logins.append(
                    self._criar_login_objeto(login)
                )
            return list_logins
        
    def atualizar_login(self, id: int, username: str, password: str):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Login).filter(Login.id == id).one_or_none()
            if data:
                data.id = id
                data.username = username
                data.password = password
                db_connection.session.commit()
                return self._criar_login_objeto(data)
            return None

    def deletar_login(self, id: int):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Login).filter(Login.id == id).one_or_none()
            if  data is not None:
                db_connection.session.delete(data)
                db_connection.session.commit()
                return self._criar_login_objeto(data)
            return data