#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template

app = Flask(__name__)

dummy_base = [{
    "google_id": "wrOQLV6xB-wC",
    "title": "Harry Potter and the Sorcerer's Stone",
    "isbn": "9781781100486",
    "publication_date": "2015-12-08",
    "image_url": "https://books.google.com/books/content/images/frontcover/wrOQLV6xB-wC?fife=w500",
    "description": "\"Turning the envelope over, his hand trembling, Harry saw a purple wax seal bearing a coat of arms; a lion, an eagle, a badger and a snake surrounding a large letter 'H'.\" Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry's eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin!",
    "publishers": [
        {
            "wikipedia_url": "https://en.wikipedia.org/wiki/Pottermore",
            "name": "Pottermore",
            "description": "Pottermore is the digital publishing, e-commerce, entertainment, and news company from J.K. Rowling and is the global digital publisher of Harry Potter and J.K. Rowling's Wizarding World.",
            "owner": "J. K. Rowling",
            "image_url": "http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Pottermore.png/225px-Pottermore.png",
            "website": "http://www.pottermore.com\nshop.pottermore.com"
        }
    ],
    "authors": [
        {
            "born": "1965-07-31",
            "name": "J. K. Rowling",
            "education": "Bachelor of Arts",
            "nationality": "British",
            "description": "Joanne \"Jo\" Rowling, OBE, FRSL, pen names J. K. Rowling and Robert Galbraith, is a British novelist, screenwriter and film producer best known as the author of the Harry Potter fantasy series. ",
            "alma_mater": "University of Exeter",
            "wikipedia_url": "https://en.wikipedia.org/wiki/J._K._Rowling",
            "image_url": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/220px-J._K._Rowling_2010.jpg"
        }
    ]
},
{
    "google_id": "aWZzLPhY4o0C",
    "title": "The Fellowship of the Ring",
    "isbn": "9780547952017",
    "publication_date": "2012-02-15",
    "subtitle": "Being the First Part of The Lord of the Rings",
    "image_url": "https://books.google.com/books/content/images/frontcover/aWZzLPhY4o0C?fife=w500",
    "description": "The first volume in J.R.R. Tolkien's epic adventure THE LORD OF THE RINGS One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them In ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power so that he could rule all others. But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him. After many ages it fell into the hands of Bilbo Baggins, as told in The Hobbit. In a sleepy village in the Shire, young Frodo Baggins finds himself faced with an immense task, as his elderly cousin Bilbo entrusts the Ring to his care. Frodo must leave his home and make a perilous journey across Middle-earth to the Cracks of Doom, there to destroy the Ring and foil the Dark Lord in his evil purpose. \u201cA unique, wholly realized other world, evoked from deep in the well of Time, massively detailed, absorbingly entertaining, profound in meaning.\u201d \u2013 New York Times",
    "publishers": [
        {
            "founded": "1832",
            "name": "Houghton Mifflin Harcourt",
            "location": "Boston, Massachusetts",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Houghton_Mifflin_Harcourt",
            "description": "Houghton Mifflin Harcourt is an educational and trade publisher in the United States. Headquartered in Boston's Back Bay, it publishes textbooks, instructional technology materials, assessments, reference works, and fiction and non-fiction for both young readers and adults.",
            "parent company": "Vivendi (2001\u20132002)",
            "image_url": "http://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Houghton_MHarcourt_2012logo.png/220px-Houghton_MHarcourt_2012logo.png",
            "website": "http://www.hmhco.com"
        }
    ],
    "authors": [
        {
            "born": "1892-01-03",
            "name": "J. R. R. Tolkien",
            "nationality": "British",
            "description": "John Ronald Reuel Tolkien CBE FRSL, known by his pen name J. R. R. Tolkien, was an English writer, poet, philologist, and university professor who is best known as the author of the classic high-fantasy works The Hobbit, The Lord of the Rings, and The Silmarillion.\n",
            "alma_mater": "Exeter College, Oxford",
            "died": "1973-09-02",
            "wikipedia_url": "https://en.wikipedia.org/wiki/J._R._R._Tolkien",
            "image_url": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Tolkien_1916.jpg/220px-Tolkien_1916.jpg"
        }
    ]
},
{
    "google_id": "L0hFAwAAQBAJ",
    "title": "A Memory of Light",
    "isbn": "9780765325952",
    "publication_date": "2013-01-08",
    "image_url": "https://books.google.com/books/content/images/frontcover/L0hFAwAAQBAJ?fife=w500",
    "description": "In the conclusion to the \"Wheel of Time\" series, all of humanity is in peril as Rand al'Thor moves forward to break the seals on the Dark One's prison and the Last Battle will determine the fate of the world.",
    "publishers": [
        {
            "founded": "2000",
            "name": "Palgrave Macmillan",
            "location": "London",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Palgrave_Macmillan",
            "description": "Palgrave Macmillan is an international academic and trade publishing company. Its programme includes textbooks, journals, monographs, professional and reference works in print and online.\nPalgrave Macmillan was created in 2000 when St. ",
            "parent company": "Springer Nature",
            "website": "http://www.palgrave.com"
        }
    ],
    "authors": [
        {
            "born": "1948-10-17",
            "name": "Robert Jordan",
            "died": "2007-09-16",
            "description": "James Oliver Rigney, Jr., better known by his pen name Robert Jordan, was an American author of epic fantasy. He is best known for the Wheel of Time series, which comprises 14 books and a prequel novel. ",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Robert_Jordan",
            "image_url": "http://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Robert_Jordan.jpg/250px-Robert_Jordan.jpg"
        },
        {
            "born": "1975-12-19",
            "name": "Brandon Sanderson",
            "nationality": "American",
            "description": "Brandon Sanderson is an American fantasy and science fiction writer. He is best known for his Mistborn series and his work in finishing Robert Jordan's epic fantasy series The Wheel of Time. ",
            "alma_mater": "Brigham Young University (B.A., M.A.)",
            "wikipedia_url": "https://en.wikipedia.org/wiki/Brandon_Sanderson",
            "image_url": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Brandon_Sanderson_sign.jpg/250px-Brandon_Sanderson_sign.jpg"
        }
    ]
}
]

@app.route('/books/<string:requested_book>')
def books(requested_book):
    # point to right book
    book = None # book doesn't exist by default
    for cur_book in dummy_base:
        if requested_book == cur_book["title"]:
            book = requested_book

            # determine related books
            break # book was found, book will be the last item before break

    if book:
        related = []
        for book_ in dummy_base:
            if cur_book['authors'][0]['name'] == book_['authors'][0]['name']:
                if cur_book['title'] != book_['title']:
                    related.append(book_['image_url'])
                    
        return render_template("book_template.html", book = cur_book, related = related[:3])
    return "Book does not exist"

@app.route('/')
def index():
    return render_template("index.html", dummy_base = dummy_base)

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
