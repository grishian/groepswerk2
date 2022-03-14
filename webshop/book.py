from sqlalchemy import Column, String
from database import BaseObject, session

class Book(BaseObject):
    __tablename__ = 'T_BOOK'

    type = Column('F_TYPE', String(50), nullable = False) # dropdown menu
    title = Column('F_TITLE', String(300), nullable = False)
    author = Column('F_AUTHOR', String(50), nullable = False)
    isbn = Column('F_ISBN', String(13), nullable = False, unique = True)
    genre = Column('F_GENRE', String(50), nullable = False) # dropdown menu
    price = Column('F_PRICE', String(15), nullable = True)
    language = Column('F_LANGUAGE', String(50), nullable = False) # dropdown menu
    series = Column('F_SERIES', String (200), nullable = True)
    size = Column('F_SIZE', String(50), nullable = False) # size stands for pages, length(minutes), characters

    def __str__(self):
        pass
    #some methods ...


def add_book():
    b = Book()
    print('Adding book...')

    b.type = input('Choose book type: ') # dropdown menu
    b.title = input('Give book title: ')
    b.author = input('Give author name: ')
    b.isbn = input('Give isbn-number: ')
    b.genre = input('Choose book genre: ') # dropdown menu
    b.price = input('Give sale price: ')
    b.language = input('Choose language: ') # dropdown menu
    b.series = input('Give book series: ')
    b.size = input('Give book size: ') # possibly: dropdown menu to put in size in pages, length(minutes) or characters

    session.add(b)
    session.commit()


