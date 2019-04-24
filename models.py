# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemy as wa
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres@localhost:5432/book_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
app.config['WHOOSH_BASE'] = 'whoosh'
db = SQLAlchemy(app)

#Creating a relational table to link up data acros tables in our database
book_rel = db.Table('book_rel',
    db.Column('author_name', db.String(), db.ForeignKey('author.name')),
    db.Column('google_id', db.String(), db.ForeignKey('book.google_id')),
    db.Column('pub_name', db.String(), db.ForeignKey('publisher.name'))
)

#This class models the structure of the table Book.
#Books are stored in rows with attributes of the book arranged in column. Primary key for identification and query is the book's google id
#Attributes include title, google_id, isbn, date, image and description as well as written by (author) and publisher'd info

class Book(db.Model):
    __tablename__ = 'book'
    __searchable__ = ['title', 'description']

    google_id = db.Column(db.String(80), primary_key = True)
    title = db.Column(db.String(80), nullable = True)
    isbn = db.Column(db.String(), nullable = True)
    publication_date = db.Column(db.String(80), nullable = True)
    image_url = db.Column(db.String(80), nullable = True)
    description = db.Column(db.String(), nullable = True)

    # relationships
    written_by = db.relationship('Author', secondary=book_rel, backref=db.backref('written_by', lazy='dynamic'))
    published_by = db.relationship('Publisher', secondary=book_rel, backref=db.backref('published_by', lazy='dynamic'))


#This class models the structure of the table Author.
#Authors are stored in rows with attributes of the author arranged in column. Primary key for identification and query is the author's name
#Attributes include name, born, education, nationality, description, alma_mater, wiki_url, and image. These attributes are nullable
class Author(db.Model):
    __tablename__ = 'author'
    __searchable__ = ['name', 'description']

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
#wa.whoosh_index(app, Author)

# The structure is same as table Book and Author.
class Publisher(db.Model):
    __tablename__ = 'publisher'
    __searchable__ = ['name', 'owner', 'parent_company']

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
#wa.whoosh_index(app, Publisher)

#db.create_all()
# End of models.py


# wa.whoosh_index(app, Book)
# wa.whoosh_index(app, Publisher)
# wa.whoosh_index(app, Author)
