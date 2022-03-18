from database import session
from book import Book
from ebook import EBook
from audiobook import AudioBook
from physicalbook import PhysicalBook

def add_book():
    print('Adding book...')
    b = Book()
    b.type = input('Which type of book would you like to add? Choose from "ebook", "audiobook" or "physicalbook": ')
    if b.type == 'ebook':
        b = EBook()
        b.title = input('Give book title: ')
        b.author = input('Give author name: ')
        b.isbn = input('Give isbn-number: ')
        b.genre = input('Choose book genre: ') 
        b.price = input('Give sale price: ')
        b.language = input('Choose language: ') 
        b.series = input('Give book series: ')
        b.size = input('Give book size (in characters): ') 
        session.add(b)
        session.commit()
    if b.type == 'audiobook':
        b = AudioBook()
        b.title = input('Give book title: ')
        b.author = input('Give author name: ')
        b.isbn = input('Give isbn-number: ')
        b.genre = input('Choose book genre: ') 
        b.price = input('Give sale price: ')
        b.language = input('Choose language: ') 
        b.series = input('Give book series: ')
        b.size = input('Give book size (in minutes): ') 
        session.add(b)
        session.commit()
    if b.type == 'physicalbook':
        b = PhysicalBook()
        b.title = input('Give book title: ')
        b.author = input('Give author name: ')
        b.isbn = input('Give isbn-number: ')
        b.genre = input('Choose book genre: ') 
        b.price = input('Give sale price: ')
        b.language = input('Choose language: ') 
        b.series = input('Give book series: ')
        b.size = input('Give book size (in pages): ') 
        session.add(b)
        session.commit()

#add_book()