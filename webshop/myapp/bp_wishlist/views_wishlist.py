from myapp import db
from myapp.bp_wishlist import bp_wishlist
from flask import render_template, url_for, flash
from flask_login import login_required, current_user
from myapp.bp_wishlist.model_wishlist import Wishlist
from myapp.bp_book.model_book import Book


@bp_wishlist.route('/wishlist')
def do_wishlist():
    return render_template('wishlist/wishlist.html')


@bp_wishlist.route('/add_to_my_wishlist/<isbn>', methods=["GET", "POST"])
@login_required
def add_to_wishlist(isbn):

    book = Book.query.filter_by(isbn=isbn).first_or_404()
    user_id = current_user.id

    wishlist_item = Wishlist()
    wishlist_item.book_id = isbn
    wishlist_item.user_id = user_id

    db.session.add(wishlist_item)
    db.session.commit()


    flash('Book:{} added to your wishlist'.format(book.title), 'OK')

    return render_template('wishlist/wishlist.html')





