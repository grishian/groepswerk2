from sqlalchemy import Column, String
from database import BaseObject, session
from book import Book

class PhysicalBook(Book):

    __tablename__ = 'T_PHYSICALBOOK'

    type = Column('F_TYPE', String(50), nullable = False, default='physical') # fixed type
    size = Column('F_SIZE', String(50), nullable = False, default='200 pages') # size in pages




    def __str__(self):
        pass
    #some methods ...

session.commit()