def test_new_book():
    from myapp.bp_book.model_book import Book
    '''
    GIVEN a book model
    WHEN a new book is created
    THEN check if fields are defined correctly
    '''

    book = Book()
    book.type


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
