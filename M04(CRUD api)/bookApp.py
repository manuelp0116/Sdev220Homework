from flask import Flask
from flask_sqlalchemy import SQLAlchemy

book_app = Flask(__name__)
db = SQLAlchemy()

book_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bookData.db"
db.init_app(book_app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    book_author = db.Column(db.String(100), unique=True, nullable=False)
    book_publisher = db.Column(db.String(100))
    
    def __repr__(self):
        return f"{self.book_name} - {self.book_author}"

with book_app.app_context():
    db.create_all()
    
@book_app.route('/')
def index():
    return "hello, world!"

with book_app.app_context():
    db.create_all()
