from flask_restx import fields

from .extensions import api


book_schema = api.model("Book",{
    'id':fields.Integer,
    'title':fields.String,
    'locccn':fields.Integer
    # 'user':fields.Nested(user_schema)
})

user_schema = api.model("User",{
    "id":fields.Integer,
    "username":fields.String,
    "books":fields.List(fields.Nested(book_schema))

})

user_creation_schema = api.model("UserCreation",{
    "username":fields.String
})

book_creation_schema = api.model("BookCreation",{
    "title":fields.String,
    "user_id":fields.Integer,
    "locccn":fields.Integer
})