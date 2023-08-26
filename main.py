from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os,json
from flask_restx import Api,Resource,reqparse,inputs,fields


base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
api = Api(app)

request_model = api.model('RequestModel',{
    "username":fields.String(required=True,description="Username field is required"),
    "email":fields.String(type=inputs.email,description="Email field is necessary")
})

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username =  db.Column(db.String(length=200), unique=True)
    email = db.Column(db.String)
    books = db.relationship('Book',backref='users',lazy=True)

    def __repr__(self):
        return f"UID:{self.id} {self.username}"

class Book(db.Model):
    __tablename__  = "books"
    id = db.Column(db.Integer,primary_key=True)
    locccn = db.Column(db.Integer)
    title = db.Column(db.Integer,unique=True)
    owner_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    def __repr__(self):
        return self.title

todos = {}

#Data validator for Query parameters
user_parser = reqparse.RequestParser()
user_parser.add_argument('username',type=str,required=True,help="Name can not be blank")
user_parser.add_argument('email',type=inputs.email,required=False,help="Email is optional")

#Views

@api.route("/api/users")
class User(Resource):
    @api.expect(request_model,validate=True)
    def post(self):
        data = api.payload
        username = data["username"]
        email = data["email"]
        print("User details",[username,email])
        user = User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        # db.session.refresh(user)
        return {"success":{"username":username,"email":email}}

# @api.route("/todo")
# class Todo_all(Resource):
#     def get(self):
#         users=  User.query.all()
#         return users


# @api.route("/todo/<int:todo_id>")
# class Todo(Resource):
#     def get(self,todo_id):
#         return {"todo":todos[todo_id]},200
    
#     def put(self,todo_id):
#         todos[todo_id] = request.form['data']
#         return {"todo":todos[todo_id]},200


# @api.route("/home")
# class HelloWorld(Resource):
#     def get(self):
#         return {"Hello":"World"},200

if __name__ == "__main___":
    app.run(debug=True)