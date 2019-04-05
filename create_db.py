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
    list_googleID = []							#list of already recorded books in the DB
    list_key = ['title', 'google_id', 'isbn','publication_date','image_url','description']
    
    for oneBook in book['Books']:
        if oneBook['google_id'] in list_googleID:
          continue   									#skip this book since it already exists in DB	
        list_googleID.append(oneBook['google_id'])		#track book that has been read into DB
        newBooklist = []						#initialize list of book attributes
        keys_list = oneBook.keys()				#get keys of dict to check which attributes are missing
        for key in list_key :					#iterate through every possible attribute
          if key in keys_list:					#assign value to the attribite if it exist in the keys
            key = oneBook[key]
          else:									#otherwise assign Null value (i.e no info on that attribute)
            key = None
          newBooklist.append(key)
        
		# create a new book object utilizing the formatted data
        newBook = Book(title = newBooklist[0], google_id = newBooklist[1], isbn = newBooklist[2], date = newBooklist[3], image = newBooklist[4], description = newBooklist[5])
        
        # After I create the book, I can then add it to my session. 
        db.session.add(newBook)
        # commit the session to my DB.
        db.session.commit()
    


#============extract and format the publisher data========
#=========================================================

def create_pub():
    # implemented same algorithm as create_books
	
    book = load_json('books.json')
    
    list_pub = []
    list_pubKeys = ['name', 'wikipedia_url','description','owner','image_url','website']
   
    for oneBook in book['Books']:
       onePub = oneBook['publishers'][0]
       
       if onePub['name'] in list_pub:
          continue   #publisher info already exists
       list_pub.append(onePub['name'])
       newPubList = []
       pub_key_list = onePub.keys()
       for pub_key in list_pubKeys:
          if pub_key in pub_key_list:
             pub_key = onePub[pub_key]
          else:
             pub_key = None
          newPubList.append(pub_key)   
          
	   # create a new publisher object utilizing the formatted data
       newPub = Publisher(pub_name = newPubList[0], wiki_url = newPubList[1], pub_description = newPubList[2], pub_owner = newPubList[3], pub_image = newPubList[4], pub_website = newPubList[5])
            
			
       # After I create the publisher, I can then add it to my session
       db.session.add(newPub)
       # commit the session to my DB
       db.session.commit()
    
		
#============create and format the author data================
#=============================================================

def create_authors():
    # implemented same algorithm as create_books
	
    book = load_json('books.json')
    list_author = []
    list_authorKeys = ['name','born','education','nationality','description','alma_mater','wiki_url','image']
    
    for oneBook in book['Books']:
       oneAuthor = oneBook['authors'][0]
        
       if oneAuthor['name'] in list_author:
          continue   #author info already exists
       list_author.append(oneAuthor['name'])
       newAuthorList = []
       author_key_list = oneAuthor.keys()
       for author_key in list_authorKeys:
           if author_key in author_key_list:
              author_key = oneAuthor[author_key]
           else:
              author_key = None
           newAuthorList.append(author_key)
        
        #print(author_key_list)
        #print(newAuthorList)
		
		# create a new author object utilizing the formatted data
       newAuthor = Author(name = newAuthorList[0], born = newAuthorList[1], education = newAuthorList[2], nationality = newAuthorList[3], description = newAuthorList[4], alma_mater = newAuthorList[5], wiki_url = newAuthorList[6], image = newAuthorList[7])

        # After I create the publisher, I can then add it to my session
       db.session.add(newAuthor)
        # commit the session to my DB
       db.session.commit()
    


# create_books()
# create_pub()
# create_authors()
