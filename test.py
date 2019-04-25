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
        s = Publisher(name = 'ben', description = 'C++')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Publisher).filter_by(name = 'ben').one()
        self.assertEqual(str(r.name), 'ben')
        db.session.query(Publisher).filter_by(name = 'ben').delete()
        db.session.commit()

    # test relational tables
    def test_case_relational_tables(self):
        b = Book(google_id="29832", title="book 1")
        a = Author(name="author 1")
        p = Publisher(name="publisher 1")

        b.written_by.append(a)
        b.published_by.append(p)
        self.assertEqual(str(b.written_by[0].name), 'author 1')
        self.assertEqual(str(b.published_by[0].name), 'publisher 1')


        a.books_written.append(b)
        a.publisher.append(p)
        self.assertEqual(str(a.books_written[0].title), 'book 1')
        self.assertEqual(str(a.publisher[0].name), 'publisher 1')

        p.books_published.append(b)
        p.authors_signed.append(a)
        self.assertEqual(str(p.books_published[0].title), 'book 1')
        self.assertEqual(str(p.authors_signed[0].name), 'author 1')




    #book isbn test
    def test_case_existing_data(self):
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
