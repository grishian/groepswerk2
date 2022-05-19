from myapp import create_app


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_do_filter_order():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/filter/<alphabetic, price_desc, price_asc>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/filter/alphabetic')
        assert response.status_code == 200
        response = test_client.get('/filter/price_desc')
        assert response.status_code == 200
        response = test_client.get('/filter/price_asc')
        assert response.status_code == 200

def test_do_filter_genre():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/filter/price_desc' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/filter/fiction')
        assert response.status_code == 200
        response = test_client.get('/filter/non-fiction')
        assert response.status_code == 200
        response = test_client.get('/filter/horror')
        assert response.status_code == 200

def test_do_filter_type():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/filter/<fysical, e-book, audio-book>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/filter/fysical')
        assert response.status_code == 200
        response = test_client.get('/filter/e-book')
        assert response.status_code == 200
        response = test_client.get('/filter/audio-book')
        assert response.status_code == 200





