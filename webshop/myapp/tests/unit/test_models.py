def test_new_book():
    from myapp.bp_book.model_book import Book
    '''
    GIVEN a book model
    WHEN a new book is created
    THEN check if fields are defined correctly
    '''
    book = Book()
    book.type = 'Audiobook'
    book.title = 'Silent House'
    book.author = 'Orhan Pamuk'
    book.isbn = '25698712354'
    book.genre = 'History'
    book.price = '8.99'
    book.language = 'English'
    book.series = ''
    book.size = '288' + ' ' + 'Minutes'
    book.synopsis = 'Bestseller from one of the most known Turkish authors.'
    book.cover = 'https://media.s-bol.com/31RJX6zVAXXn/779x1200.jpg'

    assert book.type == 'Audiobook'
    assert book.title == 'Silent House'
    assert book.author = 'Orhan Pamuk'

def test_new_user():
    from myapp.bp_user.model_user import User
    '''
    GIVEN a user model
    WHEN a new user is created
    THEN check if fields are defined correctly
    '''
    user = User()
    user.email = 'test@hotmail.com'
    user.username = 'test_user'
    user.set_password('test')
    user.active = True

    assert user.check_password('test')
    assert user.is_active() == True
    assert user.is_author == False


def test_wishlist():
    from myapp.bp_wishlist.model_wishlist import Wishlist
    '''
    GIVEN a wishlist model
    WHEN a new user is created
    THEN check if wishlist fields are defined correctly
    '''
    wishlist = Wishlist()
    wishlist.id = 1
    wishlist.user_id = 3
    wishlist.book_id = 4

    assert wishlist.id == 1
    assert wishlist.user_id == 3
    assert wishlist.book_id == 4