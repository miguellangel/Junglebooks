# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:idbg20@localhost:5432/book_db1')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)
class Book(db.Model):
 __tablename__ = 'book'

 title = db.Column(db.String(80), nullable = False)
 id = db.Column(db.Integer, primary_key = True)
db.create_all()
# End of models.py 
