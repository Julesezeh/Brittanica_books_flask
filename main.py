from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os,json


base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)




app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import User,Book


#Views
@app.route("/",methods=["GET"])
def index():
    try:
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {
                "id":user.id,
                "username":user.username,
                "email":user.email,
                "books":user.books
            }
            user_list.append(user_data)
        # users = json.dumps(users)
        return jsonify({"users":user_list})
    
    except Exception as e:
        return {"Error":str(e)}


if __name__ == "__main___":
    app.run(debug=True)