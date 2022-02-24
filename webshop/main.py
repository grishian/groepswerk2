



def dorun():
    from database import create_database, Base
    from customer import add_customer

    #create_database()
    add_customer()


if __name__ == '__main__':
    dorun()


