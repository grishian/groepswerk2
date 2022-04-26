from myapp.bp_wishlist import bp_wishlist
from flask import render_template, url_for

@bp_wishlist.route('/wishlist')
def do_wishlist():
    return render_template('wishlist/wishlist.html')
