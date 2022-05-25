from myapp import create_app, db
from myapp.bp_book.model_book import Book
from myapp.bp_user.model_user import User
'''
BOOK = Book(type='Fysical book',
            title='Test_book',
            author='Grishian Gracida',
            isbn='9999',
            genre='Action',
            price='1000',
            language='NL',
            series='Testers',
            size='1000',
            synopsis='Testing a book',
            cover='')
USER = User.query.get(1)#curruntuser = USER? zodat isadmin werkt
'''


def test_book_isbn():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/book/<isbn>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    isbn = '9780385121675'  # existing isbn in database

    with flask_app.test_client() as test_client:
        response = test_client.get(f'/book/{isbn}')
        assert response.status_code == 200

    '''
def test_add_book():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/add_book' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/add_book')
        assert response.status_code == 200


def test_change_book():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/change_book/<isbn>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get(f'/change_book/{BOOK.isbn}')
        assert response.status_code == 200


def test_delete_book():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/delete_book/<isbn>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    Book.query.filter_by(isbn='9999').delete()

    db.session.commit()

    with flask_app.test_client() as test_client:
        response = test_client.get(f'/delete_book/{BOOK.isbn}')
        assert response.status_code == 200
    '''