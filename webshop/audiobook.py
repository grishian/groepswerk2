from sqlalchemy import Column, String
from database import BaseObject, session
from book import Book

class AudioBook(Book):
    __tablename__ = 'T_AUDIOBOOK'

    type = Column('F_TYPE', String(50), nullable = False) # fixed type
    size = Column('F_SIZE', String(50), nullable = False) # size in minutes




    def __str__(self):
        pass
    #some methods ...

session.commit()