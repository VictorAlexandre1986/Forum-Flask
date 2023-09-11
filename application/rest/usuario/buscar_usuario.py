import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.usuario.controller import UsuarioController

api_buscar_usuario = Namespace("usuario", description="Endpoint buscar usuario")


@api_buscar_usuario.route("/<int:id>", methods=["GET"])
class BuscarUsuarioPorId(Resource):

    def get(self, id: int):
        try:
            response = UsuarioController.buscar_usuario_por_id(id)
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


@api_buscar_usuario.route("/", methods=["GET"])
class BuscarUsuarios(Resource):

    def get(self):
        try:
            response = UsuarioController.buscar_usuarios()
            return Response(
                json.dumps(response),
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
            
