# import and open the json file
import json
from models import app, db, Book, Publisher, Author

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

# extract and format the book data
def create_books():
    book = load_json('books.json')
    list_key = ['title', 'google_id', 'isbn','publication_date','image_url','description']
    
    for oneBook in book['Books']:		
        newKeylist = []
        keys_list = oneBook.keys()
        for key in list_key :
          if key in keys_list:
            key = oneBook[key]
            newKeylist.append(key)
          else:
            key = None
        # create a new book object utilizing the formatted data
        print(newKeylist)
        newBook = Book(title = newKeylist[0], google_id = newKeylist[1], isbn = newKeylist[2], date = newKeylist[3], image = newKeylist[4], description = newKeylist[5])
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()
    print("done")
# extract and format the publisher data
def create_pub():
    book = load_json('books.json')
    pub_num = 1
    for oneBook in book['Books']:
        onePub = oneBook['publishers'][0]
        pub_name = onePub['name']
        pub_id = pub_name + ' ' +str(pub_num)
        wiki_url = onePub['wikipedia_url']
        pub_description = onePub['description']
        pub_owner = onePub['owner']
        pub_image = onePub['image_url']
        pub_website = onePub['website']
        pub_num += 1
        # create a new publisher object utilizing the formatted data
        newPub = Publisher(pub_id = pub_id, pub_name = pub_name, wiki_url = wiki_url, pub_description = pub_description, pub_owner = pub_owner, pub_image = pub_image, pub_website = pub_website)

        # After I create the publisher, I can then add it to my session
        db.session.add(newPub)
        # commit the session to my DB
        db.session.commit()
    print('done')
		
# create and format the author data
def create_authors():
    book = load_json('books.json')
    author_num = 1
    for oneBook in book['Books']:
        oneAuthor = oneBook['authors'][0]
        name = oneAuthor['name']
        author_id = name +' '+ str(author_num)
        born = oneAuthor['born']
        education = oneAuthor['education']
        nationality = oneAuthor['nationality']
        description = oneAuthor['description']
        alma_mater = oneAuthor['alma_mater']
        wiki_url = oneAuthor['wikipedia_url']
        image = oneAuthor['image_url']
        author_num += 1
        # create a new author object utilizing the formatted data
        newAuthor = Author(author_id = author_id, name = name, born = born, education = education, nationality = nationality, description = description, alma_mater = alma_mater, wiki_url = wiki_url, image = image)

        # After I create the publisher, I can then add it to my session
        db.session.add(newAuthor)
        # commit the session to my DB
        db.session.commit()
    print('done')


create_books()
create_pub()
create_authors()
