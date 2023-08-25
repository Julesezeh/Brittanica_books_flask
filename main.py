from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os,json
from flask_restx import Api,Resource


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
#Views
# @app.route("/",methods=["GET"])
# def index():
#     try:
#         users = User.query.all()
#         user_list = []
#         for user in users:
#             user_data = {
#                 "id":user.id,
#                 "username":user.username,
#                 "email":user.email,
#                 "books":user.books
#             }
#             user_list.append(user_data)
#         # users = json.dumps(users)
#         return jsonify({"users":user_list})
    
#     except Exception as e:
#         return {"Error":str(e)}

@api.route("/todo")
class Todo_all(Resource):
    def get(self):
        return todos


@api.route("/todo/<int:todo_id>")
class Todo(Resource):
    def get(self,todo_id):
        return {"todo":todos[todo_id]}
    
    def put(self,todo_id):
        todos[todo_id] = request.form['data']
        return {"todo":todos[todo_id]}


@api.route("/home")
class HelloWorld(Resource):
    def get(self):
        return {"Hello":"World"}

if __name__ == "__main___":
    app.run(debug=True)