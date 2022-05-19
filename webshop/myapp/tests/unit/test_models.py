from myapp.bp_user.model_user import User

def test_new_user():
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



