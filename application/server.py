from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from application.rest.pergunta.criar_pergunta import api_criar_pergunta
from application.rest.pergunta.deletar_pergunta import api_deletar_pergunta
from application.rest.pergunta.buscar_pergunta import api_buscar_pergunta
from application.rest.pergunta.atualizar_pergunta import api_atualizar_pergunta
from application.rest.usuario.criar_usuario import api_criar_usuario
from application.rest.usuario.deletar_usuario import api_deletar_usuario
from application.rest.usuario.buscar_usuario import api_buscar_usuario
from application.rest.usuario.atualizar_usuario import api_atualizar_usuario
from application.rest.resposta.criar_resposta import api_criar_resposta
from application.rest.resposta.deletar_resposta import api_deletar_resposta
from application.rest.resposta.buscar_resposta import api_buscar_resposta
from application.rest.resposta.atualizar_resposta import api_atualizar_resposta
from application.rest.login.criar_login import api_criar_login
from application.rest.login.atualizar_login import api_atualizar_login
from application.rest.login.deletar_login import api_deletar_login
from application.rest.login.buscar_login import api_buscar_login



class ServeApplication:

    def __init__(self):
        self.app = Flask(__name__)
        self._blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

    def _init_blueprints(self, app):
        api = Api(
            self._blueprint,
            title="Forum",
            version="0.0.1",
            doc="/docs",
        )

        api.add_namespace(api_criar_pergunta)
        api.add_namespace(api_deletar_pergunta)
        api.add_namespace(api_atualizar_pergunta)
        api.add_namespace(api_buscar_pergunta)
        api.add_namespace(api_criar_usuario)
        api.add_namespace(api_deletar_usuario)
        api.add_namespace(api_atualizar_usuario)
        api.add_namespace(api_buscar_usuario)
        api.add_namespace(api_criar_resposta)
        api.add_namespace(api_deletar_resposta)
        api.add_namespace(api_atualizar_resposta)
        api.add_namespace(api_buscar_resposta)
        api.add_namespace(api_criar_login)
        api.add_namespace(api_atualizar_login)
        api.add_namespace(api_deletar_login)
        api.add_namespace(api_buscar_login)
        
        app.register_blueprint(self._blueprint)

    def create_app(self):
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

        self._init_blueprints(self.app)
        CORS(self.app)

        return self.app


app = ServeApplication().create_app()