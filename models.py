# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:idbg20@localhost:5432/book_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

class Book(db.Model):
 __tablename__ = 'book'

 title = db.Column(db.String(80), nullable = False)
 google_id = db.Column(db.String(80), primary_key = True)
 isbn = db.Column(db.BigInteger, nullable = True)
 date = db.Column(db.String(80), nullable = True)
 image = db.Column(db.String(80), nullable = True)
 description = db.Column(db.String(), nullable = True)
 
class Publisher(db.Model):
 __tablename__ = 'publisher'
 pub_id = db.Column(db.String(80), primary_key = True)
 pub_name = db.Column(db.String(80), nullable = False)
 wiki_url = db.Column(db.String(), nullable = False)
 pub_description = db.Column(db.String(), nullable = False)
 pub_owner = db.Column(db.String(), nullable = False)
 pub_image = db.Column(db.String(), nullable = False)
 pub_website = db.Column(db.String(), nullable = False)

class Author(db.Model):
 __tablename__ = 'author'
 author_id = db.Column(db.String(80), primary_key = True)
 name = db.Column(db.String(80), nullable = False)
 born = db.Column(db.String(), nullable = False)
 education = db.Column(db.String(), nullable = False)
 nationality = db.Column(db.String(), nullable = False)
 description = db.Column(db.String(), nullable = False)
 alma_mater = db.Column(db.String(), nullable = False)
 wiki_url = db.Column(db.String(), nullable = False)
 image = db.Column(db.String(), nullable = False)

db.create_all()
# End of models.py 
