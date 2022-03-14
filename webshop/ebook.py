from sqlalchemy import Column, String
from database import BaseObject, session

class EBook(BaseObject):
    __tablename__ = 'T_EBOOK'

    type = Column('F_TYPE', String(50), nullable = False) # fixed type
    size = Column('F_SIZE', String(50), nullable = False) # size in characters




    def __str__(self):
        pass
    #some methods ...

session.commit()