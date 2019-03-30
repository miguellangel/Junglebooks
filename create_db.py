# import and open the json file
import json
from models import app, db, Book

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

# extract and format the book data
def create_books():
    book = load_json('books.json')

    for oneBook in book['Books']:
        title = oneBook['title']
        google_id = oneBook['google_id']
        isbn = oneBook['isbn']
        if isbn == None:
            isbn = google_id
        date = oneBook['publication_date']
        image = oneBook['image_url']
        description = oneBook['description']

        # create a new book object utilizing the formatted data
        newBook = Book(title = title, google_id = google_id, ibsn = ibsn, date = date, image = image, description = description)
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()

# extract and format the publisher data
def create_pub():
    book = load_json('books.json')

    for oneBook in book['Books']:
        onePub = oneBook['publishers'][0]
        pub_name = onePub['name']
        wiki_url = onePub['wikipedia_url']
        pub_description = onePub['description']
        pub_owner = onePub['owner']
        pub_image = onePub['image_url']
        pub_website = onePub['website']

        # create a new publisher object utilizing the formatted data
        newPub = Publisher(name = name, wiki_url = wiki_url, pub_description = pub_description, pub_owner = pub_owner, pub_image = pub_image, pub_website = pub_website)

        # After I create the publisher, I can then add it to my session
        db.session.add(newPub)
        # commit the session to my DB
        db.session.commit()

# create and format the author data
def create_authors():
    book = load_json('books.json')

    for oneBook in book['Books']:
        oneAuthor = oneBook['authors'][0]
        name = oneAuthor['name']
        born = oneAuthor['born']
        education = oneAuhtor['education']
        nationality = oneAuthor['nationality']
        description = oneAuthor['description']
        alma_mater = oneAuthor['alma_mater']
        wiki_url = oneAuthor['wikipedia_url']
        image = oneAuthor['image_url']

        # create a new author object utilizing the formatted data
        newAuthor = Author(name = name, born = born, education = education, nationality = nationality, description = description, alma_mater = alma_mater, wiki_url = wiki_url, image = image)

        # After I create the publisher, I can then add it to my session
        db.session.add(newPub)
        # commit the session to my DB
        de.session.commit()


create_books()
create_pub()
create_authors()
