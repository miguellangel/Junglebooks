#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template

from models import app, db, Book, Author, Publisher

@app.route('/publishers/<string:requested_publisher>')
def publishers(requested_publisher):
    publisher = None
    for cur_book in dummy_base:
        if requested_publisher == cur_book["publishers"][0]["name"]:
            publisher = requested_publisher
            break
    if publisher:
        return render_template("publisher_template.html", book = cur_book)
    return "Publisher not found"

@app.route('/authors/<string:requested_author>')
def authors(requested_author):
    author_db = Author.query.filter_by(name=requested_author)
    print(author_db)
    if author:
        related = []
        for book_ in dummy_base:
            if cur_book['authors'][0]['name'] == book_['authors'][0]['name']:
                if cur_book['title'] != book_['title']:
                    related.append(book_['image_url'])

        return render_template("author_template.html", book = cur_book, related = related[:3])
    return "Author not found"

@app.route('/books/<string:requested_book>')
def books(requested_book):
    # search for book in database
    db_book = Book.query.filter_by(title=requested_book).all()[0]
    if db_book:
        #find related books!!!
        return render_template("book_template.html", book = db_book)
    else:
        return "Book does not exist"
@app.route('/')
def index():
    # limit the number of covers per page
    book_db = Book.query.all()
    books_per_page = 6
    return render_template("index.html", books = book_db[:books_per_page])

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/statistics')
def statistics():
	return render_template("statistics.html")

@app.route('/books/Harry-Potter-and-the-Sorcerers-Stone')
def wrOQLV6xBwC():
	return render_template("Harry-Potter-and-the-Sorcerers-Stone.html")

@app.route('/books/A-Memory-of-Light')
def L0hFAwAAQBAJ():
	return render_template("A-Memory-of-Light.html")

@app.route('/books/the-Fellowship-of-the-Ring')
def aWZzLPhY4o0C():
	return render_template("the-Fellowship-of-the-Ring.html")

@app.route('/book1/author')
def jkrowling():
	return render_template("jkrowling.html")

@app.route('/book2/author1')
def rjordan():
	return render_template("rjordan.html")

@app.route('/book2/author2')
def bsanderson():
	return render_template("bsanderson.html")

@app.route('/book3/author')
def jrrtolkein():
	return render_template("jrrtolkein.html")

@app.route('/book1/publisher')
def pottermore():
	return render_template("Pottermore.html")

@app.route('/book2/publisher')
def pmacmillan():
	return render_template("PMacmillan.html")

@app.route('/book3/publisher')
def hmharcourt():
	return render_template("HMHarcourt.html")
if __name__ == "__main__":
    app.run(debug=True)

# end of main3.py
