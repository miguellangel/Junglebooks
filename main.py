#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template

app = Flask(__name__)
books = [{'title': 'Software Engineering', 'id': '1'},  \
         {'title':'Algorithm Design', 'id':'2'},        \
         {'title':'Python', 'id':'3'}]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/statistics')
def statistics():
	return render_template("statistics.html")

@app.route('/book1')
def book1():
	return render_template("book_1.html")

@app.route('/book2')
def book2():
	return render_template("book_2.html")

@app.route('/book3')
def book3():
	return render_template("book_3.html")

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
