



def dorun():
    from database import create_database,delete_tables, Base
    from customer import add_customer
    from books import add_book

    #delete_tables()
    #create_database()
    #add_customer()
    add_book()


if __name__ == '__main__':
    dorun()


