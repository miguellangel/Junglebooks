import os
import sys
import unittest
#from models import db, Book
from create_db import db, Book, Author, Publisher


class DBTestCases(unittest.TestCase):


    def test_source_insert_1(self):
        #test1
        s = Book(google_id = '20', title = 'C++')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Book).filter_by(google_id = '20').one()
        self.assertEqual(str(r.google_id), '20')

        db.session.query(Book).filter_by(google_id = '20').delete()
        db.session.commit()

        #test2
        s = Author(name = 'josh', born = 'C++')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Author).filter_by(name = 'josh').one()
        self.assertEqual(str(r.name), 'josh')

        db.session.query(Author).filter_by(name = 'josh').delete()
        db.session.commit()

        #test3
        s = Publisher(pub_name = 'ben', pub_description = 'C++')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Publisher).filter_by(pub_name = 'ben').one()
        self.assertEqual(str(r.pub_name), 'ben')

        db.session.query(Publisher).filter_by(pub_name = 'ben').delete()
        db.session.commit()


    def test_case_2(self):

        #test1
        r = db.session.query(Book).filter_by(title = "Harry Potter and the Sorcerer's Stone").one()

        self.assertEqual(str(r.title),"Harry Potter and the Sorcerer's Stone")

        #test2
        r = db.session.query(Book).filter_by(title = "Harry Potter and the Chamber of Secrets").one()

        self.assertEqual(str(r.title),"Harry Potter and the Chamber of Secrets")

        #test3
        r = db.session.query(Book).filter_by(title = "Harry Potter and the Prisoner of Azkaban").one()

        self.assertEqual(str(r.title),"Harry Potter and the Prisoner of Azkaban")

    #book isbn test
    def test_case_3(self):

        #test1
        r = db.session.query(Book).filter_by(isbn = "9781781100486").one()

        self.assertEqual(str(r.isbn),"9781781100486")

        #test2
        r = db.session.query(Book).filter_by(isbn = "0545582970").one()

        self.assertEqual(str(r.isbn),"0545582970")

        #test3
        r = db.session.query(Book).filter_by(isbn = "9781781100257").one()

        self.assertEqual(str(r.isbn),"9781781100257")



if __name__ == '__main__':
    unittest.main()
