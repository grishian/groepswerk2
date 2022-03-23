from config import USER_NAME, PASSWORD, HOST, PORT
from sqlalchemy import create_engine, text, Column, DateTime, Integer
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_connection = create_engine('mariadb+mariadbconnector://{}:{}@{}:{}/webshop'.format(USER_NAME, PASSWORD,
                                                                                       HOST, PORT), echo=True)
database_connection.connect()

Session = sessionmaker(bind = database_connection)
session = Session()

Base = declarative_base()

class BaseObject(Base):
    __abstract__ = True

    id = Column('PK_ID', Integer, primary_key=True, index=True)
    created_on = Column('F_CREATEON', DateTime, default=datetime.datetime.now())
    updated_on = Column('F_UPDATEDON', DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())


def create_database(engine=None, do_erase=False):
    from customer import BaseObject
    from wishlist import BaseObject
    
    if engine is None:
        engine = database_connection

    if do_erase is True:  # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which
        # Book.__table__.drop(bind=database_connection)
        # Customer.__table__.drop(bind=database_connection)
        Base.metadata.drop_all(bind=engine)

    # create tables
    Base.metadata.create_all(engine)

def delete_tables():
    from customer import Customer
    from book import Book


    #Base.metadata.drop_all(database_connection)

    Book.__table__.drop(bind=database_connection)
    Customer.__table__.drop(bind=database_connection)



    print('Tables deleted.')

def insert_customer_data():
    query = "LOAD DATA INFILE 'C:/Users/hande/Desktop/Syntra/group_project_2/webshop/customer_data.txt' INTO TABLE t_customer FIELDS TERMINATED BY ':' LINES TERMINATED BY '\r\n'"

    return query
    
def insert_book_data():
    query = "LOAD DATA INFILE 'book_data.txt' INTO TABLE t_book FIELDS TERMINATED BY ':' LINES TERMINATED BY '\n'"

    return query

#path to file: C:\Users\hande\Desktop\Syntra\group_project_2\webshop\customer_data.txt