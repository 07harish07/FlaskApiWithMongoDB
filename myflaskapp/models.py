from . import db

class users(db.Document):
    name = db.StringField()
    email = db.StringField()


# class Author(db.Document):
#     name = db.StringField()


# class Book(db.Document):
#     title = db.StringField()
#     author = db.DocumentField(Author)
#     year = db.IntField()