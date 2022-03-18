from sqlalchemy import Column, String
from database import BaseObject, session
from book import Book

class EBook(Book):
    __tablename__ = 'T_EBOOK'

    type = Column('F_TYPE', String(50), nullable = False, default = 'ebook')



    def __str__(self):
        pass
    #some methods ...

session.commit()