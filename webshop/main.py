from utils import print_title
from inputs import get_input_item
from database import delete_tables, create_database
from customer import add_customer
from book import add_book

def main_menu():
    print_title('Menu')
    options = {1: 'delete tables',
               2: 'add tables',
               3: 'add customer',
               4: 'add book'
               }

    for option in options:
        print('{}: {}'.format(option, options[option]))

    choice = get_input_item('What do you want to do? Give number(empty to exit): \n', 1)

    if choice == 1:
        print_title('Deleting database:')
        delete_tables()
    if choice == 2:
        print_title('Adding tables:')
        create_database()
    if choice == 3:
        print_title('Adding customer:')
        add_customer()
    if choice == 4:
        print_title('Adding book:')
        add_book()

    print_title('Finished...')



def dorun():
    from database import create_database,delete_tables, Base


    #delete_tables()
    #create_database()
    #add_customer()
    #add_book()


if __name__ == '__main__':
    dorun()


