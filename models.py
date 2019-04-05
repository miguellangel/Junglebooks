# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres@localhost:5432/book_db_test')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

book_rel = db.Table('book_rel',
    db.Column('author_name', db.String(), db.ForeignKey('author.name')),
    db.Column('google_id', db.String(), db.ForeignKey('book.google_id')),
    db.Column('pub_name', db.String(), db.ForeignKey('publisher.name'))
)

class Book(db.Model):
    __tablename__ = 'book'

    google_id = db.Column(db.String(80), primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    isbn = db.Column(db.String(), nullable = True)
    publication_date = db.Column(db.String(80), nullable = True)
    image_url = db.Column(db.String(80), nullable = True)
    description = db.Column(db.String(), nullable = True)

    # relationships
    written_by = db.relationship('Author', secondary=book_rel, backref=db.backref('written_by', lazy='dynamic'))
    published_by = db.relationship('Publisher', secondary=book_rel, backref=db.backref('published_by', lazy='dynamic'))

class Author(db.Model):
    __tablename__ = 'author'
    born = db.Column(db.String(), nullable = True)
    name = db.Column(db.String(80), primary_key= True)
    education = db.Column(db.String(), nullable = True)
    nationality = db.Column(db.String(), nullable = True)
    description = db.Column(db.String(), nullable = True)
    died = db.Column(db.String(), nullable = True)
    alma_mater = db.Column(db.String(), nullable = True)
    image_url = db.Column(db.String(), nullable = True)
    wikipedia_url = db.Column(db.String(), nullable = True)

    # relationships
    books_written = db.relationship('Book', secondary=book_rel, backref=db.backref('books_written', lazy='dynamic'))
    publisher = db.relationship('Publisher', secondary=book_rel, backref=db.backref('publisher', lazy='dynamic'))


class Publisher(db.Model):
    __tablename__ = 'publisher'
    wikipedia_url = db.Column(db.String(), nullable = True)
    name = db.Column(db.String(80), primary_key= True)
    description = db.Column(db.String(), nullable = True)
    owner = db.Column(db.String(), nullable = True)
    image_url = db.Column(db.String(), nullable = True)
    website = db.Column(db.String(), nullable = True)
    founded = db.Column(db.String(), nullable = True)
    location = db.Column(db.String(), nullable = True)
    parent_company = db.Column(db.String(), nullable = True)
    # relationships
    books_published = db.relationship('Book', secondary=book_rel, backref=db.backref('books_published', lazy='dynamic'))
    authors_signed = db.relationship('Author', secondary=book_rel, backref=db.backref('authors_signed', lazy='dynamic'))


#db.create_all()
# End of models.py
