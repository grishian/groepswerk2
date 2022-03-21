from soupsieve import select
from sqlalchemy import Column, String, delete
from database import BaseObject, session

class Book(BaseObject):
    __tablename__ = 'T_BOOK'

    type = Column('F_TYPE', String(50), nullable = False)
    title = Column('F_TITLE', String(300), nullable = False)
    author = Column('F_AUTHOR', String(50), nullable = False)
    isbn = Column('F_ISBN', String(13), nullable = False, unique = True)
    genre = Column('F_GENRE', String(50), nullable = False)
    price = Column('F_PRICE', String(15), nullable = True)
    language = Column('F_LANGUAGE', String(50), nullable = False)
    series = Column('F_SERIES', String (200), nullable = True)
    size = Column('F_SIZE', String(50), nullable = False) # size stands for pages, length(minutes), characters

    def __str__(self):
        pass
    #some methods ...

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
    
def remove_book():
    #t_book = __tablename__ = 'T_BOOK'
    #isbn = input('Which book would you like to delete? Please give in the isbn: ')
    
    #selected_books = session.query(Book).filter(b.isbn)
    #selected_books.delete()

    #selected_book = Book.query.filter_by(isbn = '{}'.format(b.isbn)).first()
    #selected_book.delete(b)

    #del_sel_book = delete(t_book).where(t_book.isbn == '{}'.format(isbn))
    #print(del_sel_book)

    session.commit()

