from sqlalchemy import Column, String
from database import BaseObject, session
import uuid #For id creation
from utils import print_title
from inputs import get_input_item



class Customer(BaseObject):
    __tablename__ = 'T_CUSTOMER'

    name = Column('F_NAME', String(50), nullable=False)
    #address = Column('F_ADDRESS', String(255))
    country = Column('F_COUNTRY', String(255))
    city = Column('F_CITY', String(255))
    street = Column('F_STREET', String(255))
    nr_extra = Column('F_NR_EXTRA', String(255))
    zip = Column('F_ZIP', String(255))

    customer_id = Column('F_CUSTOMER_ID', String(32), nullable=False, unique=True)
    phone_nr = Column('F_PHONE_NR', String(15), nullable=False)
    mail = Column('F_MAIL', String(255), nullable=False, unique=True)
    wishlist_id = Column('F_WHISLIST_id', String(15), nullable=True, unique=True)

    #create extra columns for adress: country, city, street, nr+extra, zip


    def __str__(self):
        pass
    #some methods ...

def add_customer():
    c = Customer()
    
    c.name = input('Give customer name: ')
    c.customer_id = input('Give unique customer_id: ')
    c.phone_nr = input('Give customer phone_nr: ')
    c.mail = input('Give customer mail: ')

    session.add(c)
    session.commit()


def search_customer():
    input_id = input('What customer are you looking for? Please give in the id: ')

    qry = session.query(Customer).filter_by(id=input_id)

    return qry

# change_customer function
def change_customer():
    print_title('Change a customer')

    customer_qry = search_customer()

    options = {1: 'change name',
               2: 'change country',
               3: 'change city',
               4: 'change street',
               5: 'change nr_extra',
               6: 'change zip',
               7: 'change phone_nr',
               8: 'change mail'
               }
    for option in options:
        print('{}: {}'.format(option, options[option]))

    choice = get_input_item('What do you want to do? Give number(empty to exit): \n', 1)

    if choice == 1:
        print_title('Change name:')
        customer_name = get_input_item('Give new name: ')
        customer_qry.one().name = customer_name

    '''    
    if choice == 2:
        ...
    if choice == 3:
        ...
    if choice == 4:
        ...
    if choice == 5:
        ...
    '''

    session.commit()










