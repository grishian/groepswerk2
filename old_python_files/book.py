from soupsieve import select
from sqlalchemy import Column, String, delete
from database import BaseObject, session
from utils import print_title
from inputs import get_input_item


class Book(BaseObject):
    __tablename__ = 'T_BOOK'

    type = Column('F_TYPE', String(50), nullable=False)
    title = Column('F_TITLE', String(300), nullable=False)
    author = Column('F_AUTHOR', String(50), nullable=False)
    isbn = Column('F_ISBN', String(13), nullable=False, unique=True)
    genre = Column('F_GENRE', String(50), nullable=False)
    price = Column('F_PRICE', String(15), nullable=True)
    language = Column('F_LANGUAGE', String(50), nullable=False)
    series = Column('F_SERIES', String(200), nullable=True)
    size = Column('F_SIZE', String(50), nullable=False)  # size stands for pages, length(minutes), characters

    def __str__(self):
        pass


def add_book():
    b = Book()

    b.type = input('Which type of book would you like to add? (Choose from "ebook", "audiobook" or "physicalbook"): ')
    b.title = input('Give book title: ')
    b.author = input('Give author name: ')
    b.isbn = input('Give isbn-number: ')
    b.genre = input('Choose book genre: ')
    b.price = input('Give sale price: ')
    b.language = input('Choose language: ')
    b.series = input('Give book series: ')
    b.size = input('Give book size (in characters, words or pages): ')

    session.add(b)
    session.commit()


def search_book():  # return is a qry NOT an object!

    input_isbn = input('What book are you looking for? Please give in the isbn: ')

    qry = session.query(Book).filter_by(isbn=input_isbn)

    return qry


def remove_book():
    book = search_book()
    book.delete()

    session.commit()


def change_book():  # in progress
    print_title('Change a book')

    book_qry = search_book()

    options = {1: 'change type',
               2: 'change title',
               3: 'change author',
               4: 'change isbn',
               5: 'change genre',
               6: 'change price',
               7: 'change language',
               8: 'change series',
               9: 'change size'
               }
    for option in options:
        print('{}: {}'.format(option, options[option]))

    choice = get_input_item('What do you want to do? Give number(empty to exit): \n', 1)

    if choice == 1:
        print_title('Change type:')
        book_type = get_input_item('Give new type: ')
        book_qry.one().type = book_type
    if choice == 2:
        print_title('Change title:')
        book_title = get_input_item('Give new title: ')
        book_qry.one().type = book_title
    if choice == 3:
        print_title('Change author:')
        book_author = get_input_item('Give new author: ')
        book_qry.one().type = book_author
    if choice == 4:
        print_title('Change isbn:')
        book_isbn = get_input_item('Give new isbn: ')
        book_qry.one().type = book_isbn
    if choice == 5:
        print_title('Change genre:')
        book_genre = get_input_item('Give new genre: ')
        book_qry.one().type = book_genre
    if choice == 6:
        print_title('Change price:')
        book_price = get_input_item('Give new price: ')
        book_qry.one().type = book_price
    if choice == 7:
        print_title('Change language:')
        book_lang = get_input_item('Give new language: ')
        book_qry.one().type = book_lang
    if choice == 8:
        print_title('Change series:')
        book_ser = get_input_item('Give new series: ')
        book_qry.one().type = book_ser
    if choice == 9:
        print_title('Change size:')
        book_size = get_input_item('Give new size: ')
        book_qry.one().type = book_size

    session.commit()
