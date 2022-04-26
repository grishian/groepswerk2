from sqlalchemy import Column, String, ForeignKey, Integer
from database import BaseObject, session
from customer import Customer
from book import Book


class Wishlist(BaseObject):

    __tablename__ = 'T_WISHLIST'

    FK_customer_id = Column('FK_CUSTOMER_ID', ForeignKey(Customer.id), nullable=False)
    FK_book_id = Column('FK_CUSTOMER_ID', ForeignKey(Book.id), nullable=True, Unique=True)

    def __str__(self):
        pass
    #some methods ...

#verwijder boek van wishlist functie:
def remove_book(self):
    pass


