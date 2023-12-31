from flask import Flask
from .extensions import db,api
from .resources import api_namespace

def create_app():
    
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(api_namespace)

    return app