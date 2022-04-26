from myapp.bp_user import bp_user
from flask import render_template

@bp_user.route('/user')
def do_user():
    return render_template('user/user.html')
