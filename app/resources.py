from flask_restx import Resource,Namespace

api_namespace = Namespace("api")


@api_namespace.route("/hello")
class Hello(Resource):
    pass