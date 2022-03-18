from sqlalchemy import Column, String
from database import BaseObject, session

class Book(BaseObject):
    __abstract__ = True

    type = Column('F_TYPE', String(50), nullable = False)
    title = Column('F_TITLE', String(300), nullable = False)
    author = Column('F_AUTHOR', String(50), nullable = False)
    isbn = Column('F_ISBN', String(13), nullable = False, unique = True)
    genre = Column('F_GENRE', String(50), nullable = False) # dropdown menu
    price = Column('F_PRICE', String(15), nullable = True)
    language = Column('F_LANGUAGE', String(50), nullable = False) # dropdown menu
    series = Column('F_SERIES', String (200), nullable = True)
    size = Column('F_SIZE', String(50), nullable = False) # size stands for pages, length(minutes), characters





