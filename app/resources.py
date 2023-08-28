from flask_restx import Resource,Namespace

from .schema import book_schema, user_schema, user_creation_schema, book_creation_schema
from .models import Book, User

from .extensions import db

api_namespace = Namespace("api")

@api_namespace.route("/hello")
class Hello(Resource):
    #Simply define http methods
    def get(self):
        return {"Hello":"This is being served from rest-x"}
    


@api_namespace.route("/books")
class BooksCreateListAPI(Resource):
    @api_namespace.marshal_list_with(book_schema)
    def get(self):
        return Book.query.all()
    
    @api_namespace.expect(book_creation_schema)
    @api_namespace.marshal_with(book_schema)
    def post(self):
        book = Book(title=api_namespace.payload["title"], user_id=api_namespace.payload["user_id"], locccn=api_namespace.payload["locccn"])
        db.session.add(book)
        db.session.commit()
        return book,201


@api_namespace.route("/users")    
class UserCreateListAPI(Resource):
    @api_namespace.marshal_list_with(user_schema)
    def get(self):
        return User.query.all()
    
    @api_namespace.expect(user_creation_schema)
    @api_namespace.marshal_with(user_schema)
    def post(self):
        new_user = User(username=api_namespace.payload["username"])
        db.session.add(new_user)
        db.session.commit()
        return new_user,201
    

@api_namespace.route("/users/<int:id>")
class UserDetailAPI(Resource):
    @api_namespace.marshal_with(user_schema)
    def get(self,id):
        user = User.query.get(id)
        return user
    
    @api_namespace.marshal_with(user_schema)
    @api_namespace.expect(user_creation_schema)
    def put(self,id):
        user = User.query.get(id)
        user.username = api_namespace.payload["username"]
        
        db.session.commit()
        return user,200


@api_namespace.route("/books/<int:id>")
class BookDetailAPI(Resource):
    @api_namespace.marshal_with(book_schema)
    def get(self,id):
        book = Book.query.get(id)
        return book
    
    @api_namespace.marshal_with(book_schema)
    @api_namespace.expect(book_creation_schema)
    def put(self,id):
        book = Book.query.get(id)
        book.title = api_namespace.payload["title"]
        book.user_id = api_namespace.payload["user_id"]
        book.locccn  = api_namespace.payload["locccn"]
        
        db.session.commit()
        return book,200