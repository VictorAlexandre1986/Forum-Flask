import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.resposta.controller import RespostaController

api_atualizar_resposta = Namespace("resposta", description="Endpoint atualizar resposta")


@api_atualizar_resposta.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarResposta(Resource):

    def patch(self, id: int):
        data = api_atualizar_resposta.payload
        try:
            response = RespostaController.atualizar_resposta(data,id)
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
            print(exc)
            return Response(
                json.dumps({"msg": 'Bad request'}),
                mimetype="application/json",
                status=HTTPStatus.BAD_REQUEST
            )
