from sqlalchemy import Column, String
from database import BaseObject, session
import uuid #For id creation



class Customer(BaseObject):
    __tablename__ = 'T_CUSTOMER'

    name = Column('F_NAME', String(50), nullable=False)
    address = Column('F_ADDRESS', String(255))
    customer_id = Column('F_CUSTOMER_ID', String(32), nullable=False, unique=True)
    phone_nr = Column('F_PHONE_NR', String(15), nullable=False)
    mail = Column('F_MAIL', String(255), nullable=False, unique=True)
    wishlist_id = Column('F_WHISLIST_id', String(15), nullable=True, unique=True)

    def __str__(self):
        pass
    #some methods ...

def add_customer():
    c = Customer()
    print('Adding customer...')
    c.name = input('Give customer name: ')
    c.customer_id = input('Give unique customer_id: ')
    c.phone_nr = input('Give customer phone_nr: ')
    c.mail = input('Give customer mail: ')

    session.add(c)
    session.commit()






