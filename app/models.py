from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50), unique=True)

    books = db.relationship("Book",back_populates="user")

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(70),unique=True)
    user_id = db.Column(db.ForeignKey("user.id"))

    user = db.relationship("User",back_populates="books")
