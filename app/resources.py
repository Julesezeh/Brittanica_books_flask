from flask_restx import Resource,Namespace

api_namespace = Namespace("api")


@api_namespace.route("/hello")
class Hello(Resource):
    #Simply define http methods
    def get(self):
        return {"Hello":"This is being served from rest-x"}