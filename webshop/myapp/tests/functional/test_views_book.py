'''from myapp import create_app

def test_book_isbn():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/book/<isbn>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/book/<isbn>')
        assert response.status_code == 200

'''