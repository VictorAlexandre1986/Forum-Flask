
import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.pergunta.controller import PerguntaController

api_criar_pergunta = Namespace("pergunta", description="Endpoint pergunta")


@api_criar_pergunta.route("/", methods=["POST"])
class CriarPergunta(Resource):

    def post(self):
        data = api_criar_pergunta.payload
        try:
            response = PerguntaController.criar_pergunta(data)
            return Response(
                response.json(),
                mimetype="application/json",
                status=200,
            )

        except ValidationError as exc:
            return Response(
                exc.json(),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )

        except ValueError as exc:
            return Response(
                json.dumps({'msg': exc.args[0]}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )

        except Exception as exc:
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )