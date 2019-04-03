#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    book_covers = [{
    "google_id": "wrOQLV6xB-wC",
    "title": "Harry Potter and the Sorcerer's Stone",
    "image_url": "https://books.google.com/books/content/images/frontcover/wrOQLV6xB-wC?fife=w500"
    }, {
    "google_id": "L0hFAwAAQBAJ",
    "title": "A Memory of Light",
    "image_url": "https://books.google.com/books/content/images/frontcover/L0hFAwAAQBAJ?fife=w500"
    }, {
    "google_id": "aWZzLPhY4o0C",
    "title": "The Fellowship of the Ring",
    "image_url": "https://books.google.com/books/content/images/frontcover/aWZzLPhY4o0C?fife=w500"
    }]

    return render_template("index.html", book_covers = book_covers)

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
    app.run()

# end of main3.py
