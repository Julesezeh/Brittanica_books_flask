from main import db


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
