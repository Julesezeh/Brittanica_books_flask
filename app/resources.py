from flask_restx import Resource,Namespace

from .schema import book_schema, user_schema, user_creation_schema
from .models import Book, User

from .extensions import db

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


@api_namespace.route("/users")    
class UserAPI(Resource):
    @api_namespace.marshal_list_with(user_schema)
    def get(self):
        return User.query.all()
    
    @api_namespace.expect(user_creation_schema)
    @api_namespace.marshal_with(user_schema)
    def post(self):
        print(api_namespace.payload)
        new_user = User(username=api_namespace.payload["username"])
        db.session.add(new_user)
        db.session.commit()
        return new_user,201