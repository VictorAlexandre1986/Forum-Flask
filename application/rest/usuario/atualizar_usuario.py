import json
from http import HTTPStatus

from flask import Response, request
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.usuario.controller import UsuarioController

api_atualizar_usuario = Namespace("usuario", description="Endpoint atualizar usuario")


@api_atualizar_usuario.route("/<int:id>", methods=["PATCH", "PUT"])
class AtualizarUsuario(Resource):

    def patch(self, id: int):
        data = api_atualizar_usuario.payload
        try:
            response = UsuarioController.atualizar_usuario(data,id)
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
