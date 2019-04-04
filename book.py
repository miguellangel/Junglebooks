# begin of book.py
import json

# read in all books	    
with open('DataSource.txt') as json_fp:
  book_data = json.load(json_fp)
  sample = {'Books': book_data}
json_fp.close()

# writes book into specified json format
with open('books.json', 'w') as fp:
    json.dump(sample, fp, indent=4)

#end of book.py