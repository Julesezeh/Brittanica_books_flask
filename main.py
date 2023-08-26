from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os,json
from flask_restx import Api,Resource,reqparse,inputs


base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
api = Api(app)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import User,Book

todos = {}

#Data validation
user_parser = reqparse.RequestParser()
user_parser.add_argument('username',type=str,required=True,help="Name can not be blank")
user_parser.add_argument('email',type=inputs.email,required=False,help="Email is optional")

#Views

@api.route("/api/users")
class User(Resource):
    def post(self):
        args = user_parser.parse_args(request.json)
        username = args['username']
        email = args['email']
        user = User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
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