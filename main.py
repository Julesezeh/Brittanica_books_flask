from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os,json


base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)




app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


from .models import User,Book

#Views
@app.route("/",methods=["GET"])
def index():
    try:
        users = User.query.all()
        print(users)
        users = json.dumps(users)
        return (users)
    except Exception as e:
        return {"Error":str(e)}


if __name__ == "__main___":
    app.run()