#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template

from models import app, db, Book, Author, Publisher

@app.route('/publishers/<string:requested_publisher>')
def publishers(requested_publisher):
    print('request', requested_publisher)
    publisher = Publisher.query.filter_by(name=requested_publisher).first()
    print('db pub', publisher)
    if publisher != []:
        return render_template("publisher_template.html", publisher = publisher)
    return "Publisher not found"

@app.route('/authors/<string:requested_author>')
def authors(requested_author):
    author_db = Author.query.filter_by(name=requested_author).first()
    if author_db != []:
        return render_template("author_template.html", author = author_db, related = [])
    return "Author not found"

@app.route('/books/<string:requested_book>')
def books(requested_book):
    # search for book in database
    db_book = Book.query.filter_by(title=str(requested_book)).first()
    if db_book:
        return render_template("book_template.html", book = db_book)
    else:
        return "Book does not exist"
@app.route('/')
def index():
    # limit the number of covers per page
    book_db = Book.query.all()
    books_per_page = 6
    return render_template("index.html", books = book_db)

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/statistics')
def statistics():
	return render_template("statistics.html")

if __name__ == "__main__":
    app.run(debug=True)

# end of main3.py
