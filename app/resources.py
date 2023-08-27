from flask_restx import Resource,Namespace

api_namespace = Namespace("api")

from .models import Book

@api_namespace.route("/hello")
class Hello(Resource):
    #Simply define http methods
    def get(self):
        return {"Hello":"This is being served from rest-x"}
    


@api_namespace.route("/books")
class BooksAPI(Resource):
    def get(self):
        return Book.query.all()