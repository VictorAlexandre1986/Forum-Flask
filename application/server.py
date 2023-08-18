from flask import Blueprint, Flask
from flask_cors import CORS
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from application.rest.pergunta.criar_pergunta import api_criar_pergunta
from application.rest.pergunta.deletar_pergunta import api_deletar_pergunta
from application.rest.pergunta.buscar_pergunta import api_buscar_pergunta
from application.rest.pergunta.atualizar_pergunta import api_atualizar_pergunta



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


        app.register_blueprint(self._blueprint)

    def create_app(self):
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

        self._init_blueprints(self.app)
        CORS(self.app)

        return self.app


app = ServeApplication().create_app()