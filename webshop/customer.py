from sqlalchemy import Column, String
from database import Base
import uuid #For id creation



class Customer(Base):
    __tablename__ = 'T_CUSTOMER'

    id = Column('F_ID', String(50), nullable=False, primary_key=True)
    name = Column('F_NAME', String(50), nullable=False)
    address = Column('F_ADDRESS', String(255))
    customer_id = Column('F_CUSTOMER_ID', String(32), nullable=False, unique=True)
    phone_nr = Column('F_PHONE_NR', String(15), nullable=False)
    mail = Column('F_MAIL', String(255), nullable=False, unique=True)
    wishlist_id = Column('F_WHISLIST_id', String(15), nullable=True, unique=True)
    password = Column('F_PASSWORD', String(50), nullable=False)

    #some methods ...




