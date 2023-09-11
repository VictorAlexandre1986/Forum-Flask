import json
from http import HTTPStatus

from flask import Response
from flask_restx import Namespace, Resource
from pydantic import ValidationError

from modules.login.controller import LoginController

api_buscar_login = Namespace("login", description="Endpoint buscar login")


@api_buscar_login.route("/<int:id>", methods=["GET"])
class BuscarPerguntaPorId(Resource):

    def get(self, id: int):
        try:
            response = LoginController.buscar_login_por_id(id)
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
            

@api_buscar_login.route("/", methods=["GET"])
class BuscarLogins(Resource):

    def get(self):
        try:
            response = LoginController.buscar_logins()
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
        