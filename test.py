import os
import sys
import unittest
from models import db, Book, Author, Publisher
from main3 import BookDetails

class DBTestCases(unittest.TestCase):

    def teardown(self):
        execfile("main3.py")

	# tests inserting various books into the database
	# tests that a book with no subtitle will assign "N/A" as the subtitle
    def test_source_insert_book_1(self):
        s = Book(booknum = "NoSubtitleBooknum", authornum = "NoSubtitleAuthornum", publishernum = "NoSubtitlePublishernum",title='NoSubtitleBook', subtitle = "N/A", author = 'NoSubtitleAuthor', publisher = 'NoSubtitlePublisher', publication_date = 'NoSubtitlePublication_Date', isbn = "NoSubtitleISBN", google_id = "NoSubtitleGoogleID", image_url = "NoSubtitleImageURL", description = "NoSubtitleDescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Book).filter_by(title = 'NoSubtitleBook').one()
        self.assertEqual(str(r.booknum), 'NoSubtitleBooknum')
        self.assertEqual(str(r.authornum), 'NoSubtitleAuthornum')
        self.assertEqual(str(r.publishernum), 'NoSubtitlePublishernum')
        self.assertEqual(str(r.title), 'NoSubtitleBook')
        self.assertEqual(str(r.subtitle), 'N/A')
        self.assertEqual(str(r.author), 'NoSubtitleAuthor')
        self.assertEqual(str(r.publisher), 'NoSubtitlePublisher')
        self.assertEqual(str(r.publication_date), 'NoSubtitlePublication_Date')
        self.assertEqual(str(r.isbn), 'NoSubtitleISBN')
        self.assertEqual(str(r.google_id), 'NoSubtitleGoogleID')
        self.assertEqual(str(r.image_url), 'NoSubtitleImageURL')
        self.assertEqual(str(r.description), 'NoSubtitleDescription')

        db.session.query(Book).filter_by(title = "NoSubtitleBook").delete()
        db.session.commit()

    # tests that a book with no listed image will assign an "Image not found" png in its place
    def test_source_insert_book_2(self):
        s = Book(booknum = "NoImageBooknum", authornum = "NoImageAuthornum", publishernum = "NoImagePublishernum",title='NoImageBook', subtitle = 'NoImageSubtitle', author = 'NoImageAuthor', publisher = 'NoImagePublisher', publication_date = 'NoImagePublication_Date', isbn = "NoImageISBN", google_id = "NoImageGoogleID", image_url = 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png', description = "NoImageDescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Book).filter_by(title = 'NoImageBook').one()
        self.assertEqual(str(r.booknum), 'NoImageBooknum')
        self.assertEqual(str(r.authornum), 'NoImageAuthornum')
        self.assertEqual(str(r.publishernum), 'NoImagePublishernum')
        self.assertEqual(str(r.title), 'NoImageBook')
        self.assertEqual(str(r.subtitle), 'NoImageSubtitle')
        self.assertEqual(str(r.author), 'NoImageAuthor')
        self.assertEqual(str(r.publisher), 'NoImagePublisher')
        self.assertEqual(str(r.publication_date), 'NoImagePublication_Date')
        self.assertEqual(str(r.isbn), 'NoImageISBN')
        self.assertEqual(str(r.google_id), 'NoImageGoogleID')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'NoImageDescription')

        db.session.query(Book).filter_by(title = "NoImageBook").delete()
        db.session.commit()

    # tests if the subtitle, publication date, and image url are missing
    def test_source_insert_book_3(self):
        s = Book(booknum = "NoSPIBooknum", authornum = "NoSPIAuthornum", publishernum = "NoSPIPublishernum",title='NoSPIBook', subtitle = 'N/A', author = 'NoSPIAuthor', publisher = 'NoSPIPublisher', publication_date = 'N/A', isbn = "NoSPIISBN", google_id = "NoSPIGoogleID", image_url ='https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png', description = "NoSPIDescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Book).filter_by(title = 'NoSPIBook').one()
        self.assertEqual(str(r.booknum), 'NoSPIBooknum')
        self.assertEqual(str(r.authornum), 'NoSPIAuthornum')
        self.assertEqual(str(r.publishernum), 'NoSPIPublishernum')
        self.assertEqual(str(r.title), 'NoSPIBook')
        self.assertEqual(str(r.subtitle), 'N/A')
        self.assertEqual(str(r.author), 'NoSPIAuthor')
        self.assertEqual(str(r.publisher), 'NoSPIPublisher')
        self.assertEqual(str(r.publication_date), 'N/A')
        self.assertEqual(str(r.isbn), 'NoSPIISBN')
        self.assertEqual(str(r.google_id), 'NoSPIGoogleID')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'NoSPIDescription')

        db.session.query(Book).filter_by(title = "NoSPIBook").delete()
        db.session.commit()

    # tests if everything but the book, author and publisher. 
    def test_source_insert_book_4(self):
        s = Book(booknum = "NoneBooknum", authornum = "NoneAuthornum", publishernum = "NonePublishernum",title='NoneBook', subtitle = 'N/A', author = 'NoneAuthor', publisher = 'NonePublisher', publication_date = 'N/A', isbn = "N/A", google_id = "N/A", image_url ='https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png', description = "N/A")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Book).filter_by(title = 'NoneBook').one()
        self.assertEqual(str(r.booknum), 'NoneBooknum')
        self.assertEqual(str(r.authornum), 'NoneAuthornum')
        self.assertEqual(str(r.publishernum), 'NonePublishernum')
        self.assertEqual(str(r.title), 'NoneBook')
        self.assertEqual(str(r.subtitle), 'N/A')
        self.assertEqual(str(r.author), 'NoneAuthor')
        self.assertEqual(str(r.publisher), 'NonePublisher')
        self.assertEqual(str(r.publication_date), 'N/A')
        self.assertEqual(str(r.isbn), 'N/A')
        self.assertEqual(str(r.google_id), 'N/A')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'N/A')

        db.session.query(Book).filter_by(title = "NoneBook").delete()
        db.session.commit()

    # tests inserting various authors into the database
    # tests if the author has no listed alma mater
    def test_source_insert_author_1(self):
        s = Author(booknum = "NoSchoolBooknum", authornum = "NoSchoolAuthornum", publishernum = "NoSchoolPublishernum",author = "NoSchoolAuthor", title = "NoSchoolTitle", publisher = "NoSchoolPublisher", born = "NoSchoolBorn", died = "NoSchoolDied", nationality = "NoSchoolNationality", education = "NoSchoolEducation", alma_mater = 'N/A', wikipedia_page = "NoSchoolWikipedia_page", image_url = "NoSchoolImage_URL", description = "NoSchoolDescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Author).filter_by(author = 'NoSchoolAuthor').one()
        self.assertEqual(str(r.booknum), 'NoSchoolBooknum')
        self.assertEqual(str(r.authornum), 'NoSchoolAuthornum')
        self.assertEqual(str(r.publishernum), 'NoSchoolPublishernum')
        self.assertEqual(str(r.author), 'NoSchoolAuthor')
        self.assertEqual(str(r.title), 'NoSchoolTitle')
        self.assertEqual(str(r.publisher), 'NoSchoolPublisher')
        self.assertEqual(str(r.born), 'NoSchoolBorn')
        self.assertEqual(str(r.died), 'NoSchoolDied')
        self.assertEqual(str(r.nationality), 'NoSchoolNationality')
        self.assertEqual(str(r.education), 'NoSchoolEducation')
        self.assertEqual(str(r.alma_mater), 'N/A')
        self.assertEqual(str(r.wikipedia_page), 'NoSchoolWikipedia_page')
        self.assertEqual(str(r.image_url), 'NoSchoolImage_URL')
        self.assertEqual(str(r.description), 'NoSchoolDescription')

        db.session.query(Author).filter_by(author = "NoSchoolAuthor").delete()
        db.session.commit()

    # tests if there is no image url given for the author
    def test_source_insert_author_2(self):
        s = Author(booknum = "NoImageBooknum", authornum = "NoImageAuthornum", publishernum = "NoImagePublishernum",author = "NoImageAuthor", title = "NoImageTitle", publisher = "NoImagePublisher", born = "NoImageBorn", died = "NoImageDied", nationality = "NoImageNationality", education = "NoImageEducation", alma_mater = "NoImageAlma_mater", wikipedia_page = "NoImageWikipedia_page", image_url = "https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png", description = "NoImageDescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Author).filter_by(author = 'NoImageAuthor').one()
        self.assertEqual(str(r.booknum), 'NoImageBooknum')
        self.assertEqual(str(r.authornum), 'NoImageAuthornum')
        self.assertEqual(str(r.publishernum), 'NoImagePublishernum')
        self.assertEqual(str(r.author), 'NoImageAuthor')
        self.assertEqual(str(r.title), 'NoImageTitle')
        self.assertEqual(str(r.publisher), 'NoImagePublisher')
        self.assertEqual(str(r.born), 'NoImageBorn')
        self.assertEqual(str(r.died), 'NoImageDied')
        self.assertEqual(str(r.nationality), 'NoImageNationality')
        self.assertEqual(str(r.education), 'NoImageEducation')
        self.assertEqual(str(r.alma_mater), 'NoImageAlma_mater')
        self.assertEqual(str(r.wikipedia_page), 'NoImageWikipedia_page')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'NoImageDescription')

        db.session.query(Author).filter_by(author = "NoImageAuthor").delete()
        db.session.commit()

    # tests if most of the author's information is missing
    def test_source_insert_author_3(self):
        s = Author(booknum = "NoInfoBooknum", authornum = "NoInfoAuthornum", publishernum = "NoInfoPublishernum",author = "NoInfoAuthor", title = "NoInfoTitle", publisher = "NoInfoPublisher", born = "N/A", died="N/A", nationality = "N/A", education="N/A", alma_mater = "N/A", wikipedia_page = "N/A", image_url = "https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png", description = "N/A")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Author).filter_by(author = 'NoInfoAuthor').one()
        self.assertEqual(str(r.booknum), 'NoInfoBooknum')
        self.assertEqual(str(r.authornum), 'NoInfoAuthornum')
        self.assertEqual(str(r.publishernum), 'NoInfoPublishernum')
        self.assertEqual(str(r.author), 'NoInfoAuthor')
        self.assertEqual(str(r.title), 'NoInfoTitle')
        self.assertEqual(str(r.publisher), 'NoInfoPublisher')
        self.assertEqual(str(r.born), 'N/A')
        self.assertEqual(str(r.died), 'N/A')
        self.assertEqual(str(r.nationality), 'N/A')
        self.assertEqual(str(r.education), 'N/A')
        self.assertEqual(str(r.alma_mater), 'N/A')
        self.assertEqual(str(r.wikipedia_page), 'N/A')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'N/A')

        db.session.query(Author).filter_by(author = "NoInfoAuthor").delete()
        db.session.commit()

    # tests if all of the information is given
    def test_source_insert_author_4(self):
        s = Author(booknum = "AllInfoBooknum", authornum = "AllInfoAuthornum", publishernum = "AllInfoPublishernum",author = "AllInfoAuthor", title = "AllInfoTitle", publisher = "AllInfoPublisher", born = "AllInfoBorn", died="AllInfoDied", nationality = "AllInfoNationality", education="AllInfoEducation", alma_mater = "AllInfoAlmaMater", wikipedia_page = "AllInfoWiki", image_url = "AllInfoImage", description = "AllInfoDescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Author).filter_by(author = 'AllInfoAuthor').one()
        self.assertEqual(str(r.booknum), 'AllInfoBooknum')
        self.assertEqual(str(r.authornum), 'AllInfoAuthornum')
        self.assertEqual(str(r.publishernum), 'AllInfoPublishernum')
        self.assertEqual(str(r.author), 'AllInfoAuthor')
        self.assertEqual(str(r.title), 'AllInfoTitle')
        self.assertEqual(str(r.publisher), 'AllInfoPublisher')
        self.assertEqual(str(r.born), 'AllInfoBorn')
        self.assertEqual(str(r.died), 'AllInfoDied')
        self.assertEqual(str(r.nationality), 'AllInfoNationality')
        self.assertEqual(str(r.education), 'AllInfoEducation')
        self.assertEqual(str(r.alma_mater), 'AllInfoAlmaMater')
        self.assertEqual(str(r.wikipedia_page), 'AllInfoWiki')
        self.assertEqual(str(r.image_url), 'AllInfoImage')
        self.assertEqual(str(r.description), 'AllInfoDescription')

        db.session.query(Author).filter_by(author = "AllInfoAuthor").delete()
        db.session.commit()


    # tests inserting various publishers into the database
    # tests if the publisher has no listed location
    def test_source_insert_publication_1(self):
        s = Publisher(booknum = "NoLocBooknum", authornum = "NoLocAuthornum", publishernum = "NoLocPublishernum",publisher = 'NoLocPublisher', parent_company = 'NoLocParent_Company', owner = "NoLocOwner", location = "N/A", founded = "NoLocFounded", title = "NoLocTitle", author= 'NoLocAuthor', wikipedia_page_ = 'NoLocWikipedia_Page', description = 'NoLocDescription', website = 'NoLocWebsite', image_url = "NoLocImage_URL")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Publisher).filter_by(publisher = 'NoLocPublisher').one()
        self.assertEqual(str(r.booknum), 'NoLocBooknum')
        self.assertEqual(str(r.authornum), 'NoLocAuthornum')
        self.assertEqual(str(r.publishernum), 'NoLocPublishernum')
        self.assertEqual(str(r.publisher), 'NoLocPublisher')
        self.assertEqual(str(r.parent_company), 'NoLocParent_Company')
        self.assertEqual(str(r.owner), 'NoLocOwner')
        self.assertEqual(str(r.location), 'N/A')
        self.assertEqual(str(r.founded), 'NoLocFounded')
        self.assertEqual(str(r.title), 'NoLocTitle')
        self.assertEqual(str(r.author), 'NoLocAuthor')
        self.assertEqual(str(r.wikipedia_page_), 'NoLocWikipedia_Page')
        self.assertEqual(str(r.description), 'NoLocDescription')
        self.assertEqual(str(r.website), 'NoLocWebsite')
        self.assertEqual(str(r.image_url), 'NoLocImage_URL')

        db.session.query(Publisher).filter_by(publisher = 'NoLocPublisher').delete()
        db.session.commit()

    # tests if the publisher has no given image URL
    def test_source_insert_publication_2(self):
        s = Publisher(booknum = "NoImageBooknum", authornum = "NoImageAuthornum", publishernum = "NoImagePublishernum",publisher = 'NoImagePublisher', parent_company = 'NoImageParent_Company', owner = "NoImageOwner", location = 'NoImageLocation', founded = "NoImageFounded", title = "NoImageTitle", author= 'NoImageAuthor', wikipedia_page_ = 'NoImageWikipedia_Page', description = 'NoImageDescription', website = 'NoImageWebsite', image_url = 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Publisher).filter_by(publisher = 'NoImagePublisher').one()
        self.assertEqual(str(r.booknum), 'NoImageBooknum')
        self.assertEqual(str(r.authornum), 'NoImageAuthornum')
        self.assertEqual(str(r.publishernum), 'NoImagePublishernum')
        self.assertEqual(str(r.publisher), 'NoImagePublisher')
        self.assertEqual(str(r.parent_company), 'NoImageParent_Company')
        self.assertEqual(str(r.owner), 'NoImageOwner')
        self.assertEqual(str(r.location), 'NoImageLocation')
        self.assertEqual(str(r.founded), 'NoImageFounded')
        self.assertEqual(str(r.title), 'NoImageTitle')
        self.assertEqual(str(r.author), 'NoImageAuthor')
        self.assertEqual(str(r.wikipedia_page_), 'NoImageWikipedia_Page')
        self.assertEqual(str(r.description), 'NoImageDescription')
        self.assertEqual(str(r.website), 'NoImageWebsite')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')

        db.session.query(Publisher).filter_by(publisher = 'NoImagePublisher').delete()
        db.session.commit()

    # tests if the publisher is missing most of its information
    def test_source_insert_publication_3(self):
        s = Publisher(booknum = "NoInfoBooknum", authornum = "NoInfoAuthornum", publishernum = "NoInfoPublishernum",publisher = 'NoInfoPublisher', parent_company = "N/A", owner ="N/A", location = "N/A", founded = "N/A", title = "NoInfoTitle", author = "N/A", wikipedia_page_="N/A", description="N/A", website="N/A", image_url="https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Publisher).filter_by(publisher = 'NoInfoPublisher').one()
        self.assertEqual(str(r.booknum), 'NoInfoBooknum')
        self.assertEqual(str(r.authornum), 'NoInfoAuthornum')
        self.assertEqual(str(r.publishernum), 'NoInfoPublishernum')
        self.assertEqual(str(r.publisher), 'NoInfoPublisher')
        self.assertEqual(str(r.parent_company), 'N/A')
        self.assertEqual(str(r.owner), 'N/A')
        self.assertEqual(str(r.location), 'N/A')
        self.assertEqual(str(r.founded), 'N/A')
        self.assertEqual(str(r.title), 'NoInfoTitle')
        self.assertEqual(str(r.author), 'N/A')
        self.assertEqual(str(r.wikipedia_page_), 'N/A')
        self.assertEqual(str(r.description), 'N/A')
        self.assertEqual(str(r.website), 'N/A')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')

        db.session.query(Publisher).filter_by(publisher = 'NoInfoPublisher').delete()
        db.session.commit

    # tests if the publisher has all of its information
    def test_source_insert_publication_4(self):
        s = Publisher(booknum = "AllInfoBooknum", authornum = "AllInfoAuthornum", publishernum = "AllInfoPublishernum",publisher = 'AllInfoPublisher', parent_company = "AllInfoParentCompany", owner ="AllInfoOwner", location = "AllInfoLocation", founded = "AllInfoFounded", title = "AllInfoTitle", author = "AllInfoAuthor", wikipedia_page_="AllInfoWiki", description="AllInfoDescription", website="AllInfoWebsite", image_url="AllInfoImage")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Publisher).filter_by(publisher = 'AllInfoPublisher').one()
        self.assertEqual(str(r.booknum), 'AllInfoBooknum')
        self.assertEqual(str(r.authornum), 'AllInfoAuthornum')
        self.assertEqual(str(r.publishernum), 'AllInfoPublishernum')
        self.assertEqual(str(r.publisher), 'AllInfoPublisher')
        self.assertEqual(str(r.parent_company), 'AllInfoParentCompany')
        self.assertEqual(str(r.owner), 'AllInfoOwner')
        self.assertEqual(str(r.location), 'AllInfoLocation')
        self.assertEqual(str(r.founded), 'AllInfoFounded')
        self.assertEqual(str(r.title), 'AllInfoTitle')
        self.assertEqual(str(r.author), 'AllInfoAuthor')
        self.assertEqual(str(r.wikipedia_page_), 'AllInfoWiki')
        self.assertEqual(str(r.description), 'AllInfoDescription')
        self.assertEqual(str(r.website), 'AllInfoWebsite')
        self.assertEqual(str(r.image_url), 'AllInfoImage')

        db.session.query(Publisher).filter_by(publisher = 'AllInfoPublisher').delete()
        db.session.commit()
        
    # tests if the author is missing title will assign N/A to table
    def test_source_insert_author_4(self):
        s = Author(booknum = "NoTitleBooknum", authornum = "NoTitleAuthornum", publishernum = "NoTitlePublishernum",author = "NoTitleAuthor", title = "N/A", publisher = "NoTitlePublisher", born = "NoTitleborn", died="NoTitledied", nationality = "NoTitlenationality", education="NoTitleeducation", alma_mater = "NoTitlealmamater", wikipedia_page = "NoTitlewiki", image_url = "https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png", description = "NoTitledescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Author).filter_by(author = 'NoTitleAuthor').one()
        self.assertEqual(str(r.booknum), 'NoTitleBooknum')
        self.assertEqual(str(r.authornum), 'NoTitleAuthornum')
        self.assertEqual(str(r.publishernum), 'NoTitlePublishernum')
        self.assertEqual(str(r.author), 'NoTitleAuthor')
        self.assertEqual(str(r.title), 'N/A')
        self.assertEqual(str(r.publisher), 'NoTitlePublisher')
        self.assertEqual(str(r.born), 'NoTitleborn')
        self.assertEqual(str(r.died), 'NoTitledied')
        self.assertEqual(str(r.nationality), 'NoTitlenationality')
        self.assertEqual(str(r.education), 'NoTitleeducation')
        self.assertEqual(str(r.alma_mater), 'NoTitlealmamater')
        self.assertEqual(str(r.wikipedia_page), 'NoTitlewiki')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'NoTitledescription')

        db.session.query(Author).filter_by(author = "NoTitleAuthor").delete()
        db.session.commit()


        # tests if table will read in author entries with no information other than name
    def test_source_insert_author_5(self):
        s = Author(booknum = "N/A", authornum = "N/A", publishernum = "N/A",author = "N/Aauthor", title = "N/A", publisher = "N/A", born = "N/A", died="N/A", nationality = "N/A", education="N/A", alma_mater = "N/A", wikipedia_page = "N/A", image_url = "https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png", description = "N/A")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Author).filter_by(author = 'N/Aauthor').one()
        self.assertEqual(str(r.booknum), 'N/A')
        self.assertEqual(str(r.authornum), 'N/A')
        self.assertEqual(str(r.publishernum), 'N/A')
        self.assertEqual(str(r.author), 'N/Aauthor')
        self.assertEqual(str(r.title), 'N/A')
        self.assertEqual(str(r.publisher), 'N/A')
        self.assertEqual(str(r.born), 'N/A')
        self.assertEqual(str(r.died), 'N/A')
        self.assertEqual(str(r.nationality), 'N/A')
        self.assertEqual(str(r.education), 'N/A')
        self.assertEqual(str(r.alma_mater), 'N/A')
        self.assertEqual(str(r.wikipedia_page), 'N/A')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'N/A')

        db.session.query(Author).filter_by(author = "N/Aauthor").delete()
        db.session.commit()

    #tests if table will read in author entries if no wiki exists
    def test_source_insert_author_6(self):
        s = Author(booknum = "NoWikiBooknum", authornum = "NoWikiAuthornum", publishernum = "NoWikiPublishernum",author = "NoWikiAuthor", title = "NoWikiTitle", publisher = "NoWikiPublisher", born = "NoWikiborn", died="NoWikidied", nationality = "NoWikinationality", education="NoWikieducation", alma_mater = "NoWikialmamater", wikipedia_page = "N/A", image_url = "https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png", description = "NoWikidescription")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Author).filter_by(author = 'NoWikiAuthor').one()
        self.assertEqual(str(r.booknum), 'NoWikiBooknum')
        self.assertEqual(str(r.authornum), 'NoWikiAuthornum')
        self.assertEqual(str(r.publishernum), 'NoWikiPublishernum')
        self.assertEqual(str(r.author), 'NoWikiAuthor')
        self.assertEqual(str(r.title), 'NoWikiTitle')
        self.assertEqual(str(r.publisher), 'NoWikiPublisher')
        self.assertEqual(str(r.born), 'NoWikiborn')
        self.assertEqual(str(r.died), 'NoWikidied')
        self.assertEqual(str(r.nationality), 'NoWikinationality')
        self.assertEqual(str(r.education), 'NoWikieducation')
        self.assertEqual(str(r.alma_mater), 'NoWikialmamater')
        self.assertEqual(str(r.wikipedia_page), 'N/A')
        self.assertEqual(str(r.image_url), 'https://econnect.baxter.com/assets/images/products/Renal/thumb_image_not_available.png')
        self.assertEqual(str(r.description), 'NoWikidescription')

        db.session.query(Author).filter_by(author = "NoWikiAuthor").delete()
        db.session.commit()


        # tests if the author is missing Wiki page will assign N/A to table
    def test_source_insert_publication_6(self):
        s = Publisher(booknum = "N/A", authornum = "N/A", publishernum = "N/A",publisher = 'N/APublisher', parent_company = 'N/A', owner = "N/A", location = "N/A", founded = "N/A", title = "N/A", author= 'N/A', wikipedia_page_ = 'N/A', description = 'N/A', website = 'N/A', image_url = "N/A")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Publisher).filter_by(publisher = 'N/APublisher').one()
        self.assertEqual(str(r.booknum), 'N/A')
        self.assertEqual(str(r.authornum), 'N/A')
        self.assertEqual(str(r.publishernum), 'N/A')
        self.assertEqual(str(r.publisher), 'N/APublisher')
        self.assertEqual(str(r.parent_company), 'N/A')
        self.assertEqual(str(r.owner), 'N/A')
        self.assertEqual(str(r.location), 'N/A')
        self.assertEqual(str(r.founded), 'N/A')
        self.assertEqual(str(r.title), 'N/A')
        self.assertEqual(str(r.author), 'N/A')
        self.assertEqual(str(r.wikipedia_page_), 'N/A')
        self.assertEqual(str(r.description), 'N/A')
        self.assertEqual(str(r.website), 'N/A')
        self.assertEqual(str(r.image_url), 'N/A')

        db.session.query(Publisher).filter_by(publisher = 'N/APublisher').delete()
        db.session.commit()
        
    # tests if table will read in book entries with no information other than title
    def test_source_insert_book_2(self):
        s = Book(booknum = "N/A", authornum = "N/A", publishernum = "N/A",title='N/ABook', subtitle = 'N/A', author = 'N/A', publisher = 'N/A', publication_date = 'N/A', isbn = "N/A", google_id = "N/A", image_url = 'N/A', description = "N/A")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Book).filter_by(title = 'N/ABook').one()
        self.assertEqual(str(r.booknum), 'N/A')
        self.assertEqual(str(r.authornum), 'N/A')
        self.assertEqual(str(r.publishernum), 'N/A')
        self.assertEqual(str(r.title), 'N/ABook')
        self.assertEqual(str(r.subtitle), 'N/A')
        self.assertEqual(str(r.author), 'N/A')
        self.assertEqual(str(r.publisher), 'N/A')
        self.assertEqual(str(r.publication_date), 'N/A')
        self.assertEqual(str(r.isbn), 'N/A')
        self.assertEqual(str(r.google_id), 'N/A')
        self.assertEqual(str(r.image_url), 'N/A')
        self.assertEqual(str(r.description), 'N/A')

        db.session.query(Book).filter_by(title = "N/A").delete()
        db.session.commit()

    # tests if the publisher has no listed website
    def test_source_insert_publication_5(self):
        s = Publisher(booknum = "NoWebBooknum", authornum = "NoWebAuthornum", publishernum = "NoWebPublishernum",publisher = 'NoWebPublisher', parent_company = 'NoWebParent_Company', owner = "NoWebOwner", location = "NoWebLocation", founded = "NoWebFounded", title = "NoWebTitle", author= 'NoWebAuthor', wikipedia_page_ = 'NoWebWikipedia_Page', description = 'NoWebDescription', website = 'N/A', image_url = "NoWebImage_URL")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Publisher).filter_by(publisher = 'NoWebPublisher').one()
        self.assertEqual(str(r.booknum), 'NoWebBooknum')
        self.assertEqual(str(r.authornum), 'NoWebAuthornum')
        self.assertEqual(str(r.publishernum), 'NoWebPublishernum')
        self.assertEqual(str(r.publisher), 'NoWebPublisher')
        self.assertEqual(str(r.parent_company), 'NoWebParent_Company')
        self.assertEqual(str(r.owner), 'NoWebOwner')
        self.assertEqual(str(r.location), 'NoWebLocation')
        self.assertEqual(str(r.founded), 'NoWebFounded')
        self.assertEqual(str(r.title), 'NoWebTitle')
        self.assertEqual(str(r.author), 'NoWebAuthor')
        self.assertEqual(str(r.wikipedia_page_), 'NoWebWikipedia_Page')
        self.assertEqual(str(r.description), 'NoWebDescription')
        self.assertEqual(str(r.website), 'N/A')
        self.assertEqual(str(r.image_url), 'NoWebImage_URL')

        db.session.query(Publisher).filter_by(publisher = 'NoWebPublisher').delete()
        db.session.commit()

    # tests if the publisher has no wiki
    def test_source_insert_publication_5(self):
        s = Publisher(booknum = "NoWikiBooknum", authornum = "NoWikiAuthornum", publishernum = "NoWikiPublishernum",publisher = 'NoWikiPublisher', parent_company = 'NoWikiParent_Company', owner = "NoWikiOwner", location = "NoWikiLocation", founded = "NoWikiFounded", title = "NoWikiTitle", author= 'NoWikiAuthor', wikipedia_page_ = 'N/A', description = 'NoWikiDescription', website = 'NoWikiWebsite', image_url = "NoWikiImage_URL")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Publisher).filter_by(publisher = 'NoWikiPublisher').one()
        self.assertEqual(str(r.booknum), 'NoWikiBooknum')
        self.assertEqual(str(r.authornum), 'NoWikiAuthornum')
        self.assertEqual(str(r.publishernum), 'NoWikiPublishernum')
        self.assertEqual(str(r.publisher), 'NoWikiPublisher')
        self.assertEqual(str(r.parent_company), 'NoWikiParent_Company')
        self.assertEqual(str(r.owner), 'NoWikiOwner')
        self.assertEqual(str(r.location), 'NoWikiLocation')
        self.assertEqual(str(r.founded), 'NoWikiFounded')
        self.assertEqual(str(r.title), 'NoWikiTitle')
        self.assertEqual(str(r.author), 'NoWikiAuthor')
        self.assertEqual(str(r.wikipedia_page_), 'N/A')
        self.assertEqual(str(r.description), 'NoWikiDescription')
        self.assertEqual(str(r.website), 'NoWikiWebsite')
        self.assertEqual(str(r.image_url), 'NoWikiImage_URL')

        db.session.query(Publisher).filter_by(publisher = 'NoWikiPublisher').delete()
        db.session.commit()
        


        
if __name__ == '__main__':
    unittest.main()



