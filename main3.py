#-----------------------------------------
# main3.py
# creating first flask application
#-----------------------------------------
from flask import Flask, render_template

app = Flask(__name__)
books = [{
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
    }]

@app.route('/') 
def index():
    return render_template('hello.html')

@app.route('/book2/')
def book():
    return render_template('book2.html', books = books)
if __name__ == "__main__":
    app.run()

# end of main3.py
