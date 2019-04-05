#==========import and open the json file=========
#================================================

import json
from models import app, db, Book, Publisher, Author

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

#==========extract and format the book data=======
#=================================================

def create_books():
    book = load_json('books.json')
    list_googleID = [i.google_id for i in Book.query.all()]							#list of already recorded books in the DB
    book_attrs = ['google_id', 'title', 'isbn','publication_date','image_url','description', 'publishers', 'authors']

    for oneBook in book['Books']:
        if oneBook['google_id'] in list_googleID:
            continue   									#skip this book since it already exists in DB
        newBooklist = []						#initialize list of book attributes
        keys_list = oneBook.keys()				#get keys of dict to check which attributes are missing
        for attr in book_attrs :					#iterate through every possible attribute
            if attr in keys_list:					#assign value to the attribite if it exist in the keys
                if attr == "authors":
                    # there might be more than one author
                    authors_list = oneBook[attr] # the actual list given current attr
                    for author in authors_list:
                        newAuthor = create_author(author)
                elif attr == "publishers":
                    # there might be more than one publisher
                    pub_list = oneBook[attr]
                    for pub in pub_list:
                        newPub = create_pub(pub)
                else:
                    newBooklist.append(oneBook[attr])
            else:									#otherwise assign Null value (i.e no info on that attribute)
                newBooklist.append(None) # keep order intact

		# create a new book object utilizing the formatted data
        db_books = [i.google_id for i in Book.query.all()]
        newBook = Book(google_id = newBooklist[0], title = newBooklist[1], isbn = newBooklist[2], publication_date = newBooklist[3], image_url = newBooklist[4], description = newBooklist[5])
        if newBook.google_id in db_books:
            continue # don't commit changes if book already exists

        newBook.written_by.append(newAuthor)
        newBook.published_by.append(newPub)

        newAuthor.books_written.append(newBook)
        newAuthor.publisher.append(newPub)

        newPub.books_published.append(newBook)
        newPub.authors_signed.append(newAuthor)
        # newBook.written_by.append
        # After I create the book, I can then add it to my session.
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()



#============create and format the author data================
#=============================================================

def create_author(author):
    # implemented same algorithm as create_books

    #book = load_json('books.json')
    list_author = [i.name for i in Author.query.all()]
    if author['name'] in list_author:
        return Author.query.filter_by(name=author['name']).all()[0]  #author info already exists

    author_attrs = ['name', 'born', 'education','nationality','description','died', 'alma_mater','image_url', 'wikipedia_url']


    newAuthorList = []
    author_key_list = author.keys()
    for i in author_attrs:
        if i in author_key_list:
            newAuthorList.append(author[i])
        else:
            newAuthorList.append(None) # prevent out of place appending | stick to the order
    # create a new author object utilizing the formatted data
    newAuthor = Author(name = newAuthorList[0], born = newAuthorList[1], education = newAuthorList[2], nationality = newAuthorList[3], description = newAuthorList[4], died = newAuthorList[5], alma_mater = newAuthorList[6], image_url = newAuthorList[7], wikipedia_url = newAuthorList[8])

    # After I create the publisher, I can then add it to my session
    db.session.add(newAuthor)
    # commit the session to my DB
    db.session.commit()

    return newAuthor

#============extract and format the publisher data========
#=========================================================

def create_pub(publisher):
    # instead of independently building books, accept current list of authors in current
    # iteration of create_books()

    list_pub = [i.name for i in Publisher.query.all()]
    if publisher['name'] in list_pub:
        return Publisher.query.filter_by(name=publisher['name']).all()[0] #publisher info already exists

    list_pubKeys = ['name', 'wikipedia_url','description','owner','image_url','website', 'founded', 'location', 'parent_company']

    newPubList = []
    pub_key_list = publisher.keys()

    for i in list_pubKeys:
        if i in pub_key_list:
            newPubList.append(publisher[i])
        else:
            newPubList.append(None)

    # create a new publisher object utilizing the formatted data
    newPub = Publisher(name = newPubList[0], wikipedia_url = newPubList[1], description = newPubList[2], owner = newPubList[3], image_url = newPubList[4], website = newPubList[5], founded = newPubList[6], location = newPubList[7], parent_company = newPubList[8])


    # After I create the publisher, I can then add it to my session
    db.session.add(newPub)
    # commit the session to my DB
    db.session.commit()

    return newPub


# create_books()
# create_pub()
# create_authors()
