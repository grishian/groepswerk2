from sqlalchemy import Column, String, ForeignKey, Integer
from database import BaseObject
from customer import Customer
from book import Book


class Wishlist(BaseObject):

    __tablename__ = 'T_WISHLIST'

    FK_customer_id = Column('FK_CUSTOMER_ID', ForeignKey(Customer.id), nullable=False)

    def __str__(self):
        pass
    #some methods ...
