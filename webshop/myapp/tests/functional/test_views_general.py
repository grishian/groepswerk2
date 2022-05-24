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
        response = test_client.get('/filter/Science Fiction (Sci-Fi)')
        assert response.status_code == 200
        response = test_client.get('/filter/Romance')
        assert response.status_code == 200
        response = test_client.get('/filter/Poetry')
        assert response.status_code == 200
        response = test_client.get('/filter/Non-fiction')
        assert response.status_code == 200
        response = test_client.get('/filter/Informative')
        assert response.status_code == 200
        response = test_client.get('/filter/Horror')
        assert response.status_code == 200
        response = test_client.get('/filter/History')
        assert response.status_code == 200
        response = test_client.get('/filter/Fantasy')
        assert response.status_code == 200
        response = test_client.get('/filter/Detective')
        assert response.status_code == 200
        response = test_client.get('/filter/Comic')
        assert response.status_code == 200
        response = test_client.get('/filter/Adventure')
        assert response.status_code == 200
        response = test_client.get('/filter/Action')
        assert response.status_code == 200

def test_do_filter_type():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/filter/<fysical, e-book, audio-book>' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/filter/Physical book')
        assert response.status_code == 200
        response = test_client.get('/filter/E-book')
        assert response.status_code == 200
        response = test_client.get('/filter/Audiobook')
        assert response.status_code == 200





