from flask_restx import fields

from .extensions import api

book_schema = api.model("Book",{
    'id':fields.Integer,
    'title':fields.String
})

user_schema = api.model("User",{
    "id":fields.Integer,
    "username":fields.String
})