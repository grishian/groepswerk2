



def dorun():
    from database import create_database, Base
    from customer import add_customer
    from book import add_book

    create_database()
    add_customer()
    add_book()

if __name__ == '__main__':
    dorun()


