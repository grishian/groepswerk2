from config import USER_NAME, PASSWORD, HOST, PORT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_connection = create_engine('mariadb+mariadbconnector://{}:{}@{}:{}/webshop'.format(USER_NAME, PASSWORD,
                                                                                       HOST, PORT), echo=True)
database_connection.connect()

Session = sessionmaker(bind = database_connection)
session = Session()

Base = declarative_base()


def create_database(engine=None, do_erase=False):
    from customer import Base
    if engine is None:
        engine = database_connection

    if do_erase is True:  # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which
        # Student.__table__.drop(bind=database_connection)
        # Course.__table__.drop(bind=database_connection)
        Base.metadata.drop_all(bind=engine)

    # create tables
    Base.metadata.create_all(engine)

