from myapp import db
from myapp.bp_wishlist import bp_wishlist
from flask import render_template, url_for, flash, redirect
from flask_login import login_required, current_user
from myapp.bp_wishlist.model_wishlist import Wishlist
from myapp.bp_book.model_book import Book


@bp_wishlist.route('/wishlist')
def do_wishlist():

    books = current_user.get_books_in_wishlist()

    return render_template('wishlist/wishlist.html', books=books)


@bp_wishlist.route('/add_to_my_wishlist/<isbn>', methods=["GET", "POST"])
@login_required
def add_to_wishlist(isbn):

    book = Book.query.filter_by(isbn=isbn).first_or_404()
    user_id = current_user.id
    my_wishlist_book_ids = []
    my_wishlist_items = Wishlist.query.filter_by(user_id=user_id).all()
    for wishlist_item in my_wishlist_items:
        my_wishlist_book_ids.append(wishlist_item.book_id)
    if not isbn in my_wishlist_book_ids:

        wishlist_item = Wishlist()
        wishlist_item.book_id = isbn
        wishlist_item.user_id = user_id

        db.session.add(wishlist_item)
        db.session.commit()

        flash('Book: {} added to your wishlist'.format(book.title), 'OK')
        return redirect(url_for('bp_wishlist.do_wishlist'))

    flash('Book: {} already in your wishlist'.format(book.title), 'ERROR')
    return redirect(url_for('bp_wishlist.do_wishlist'))


@bp_wishlist.route('/delete_from_my_wishlist/<isbn>', methods=["GET", "POST"])
@login_required
def delete_from_wishlist(isbn):

    book = Book.query.filter_by(isbn=isbn).first_or_404()
    user_id = current_user.id
    my_wishlist_book_ids = []
    my_wishlist_items = Wishlist.query.filter_by(user_id=user_id).all()
    for wishlist_item in my_wishlist_items:
        my_wishlist_book_ids.append(wishlist_item.book_id)

    if isbn in my_wishlist_book_ids:

        Wishlist.query.filter_by(book_id=isbn).delete()

        db.session.commit()

        flash('Book: {} deleted from your wishlist'.format(book.title), 'OK')
        return redirect(url_for('bp_wishlist.do_wishlist'))

    flash('Book: {} is not in your wishlist'.format(book.title), 'ERROR')
    return redirect(url_for('bp_wishlist.do_wishlist'))




