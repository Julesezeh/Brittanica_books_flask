from flask_restx import Resource,Namespace

from .schema import book_schema
from .models import Book

api_namespace = Namespace("api")

@api_namespace.route("/hello")
class Hello(Resource):
    #Simply define http methods
    def get(self):
        return {"Hello":"This is being served from rest-x"}
    


@api_namespace.route("/books")
class BooksAPI(Resource):
    @api_namespace.marshal_list_with(book_schema)
    def get(self):
        return Book.query.all()