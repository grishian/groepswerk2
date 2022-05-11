from myapp.bp_general import bp_general
from myapp.bp_book.model_book import Book
from flask import render_template, url_for, flash, redirect



@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    books = Book.query.all()

    return render_template('general/home.html', books=books)


@bp_general.route('/filter/<filter_by>')
def do_filter(filter_by):

    if filter_by == 'alphabetic':
        books = Book.query.order_by(Book.title).all()
    if filter_by == 'price_desc':
        books = Book.query.order_by(Book.price.desc()).all()
    if filter_by == 'price_asc':
        books = Book.query.order_by(Book.price.asc()).all()

    if filter_by == 'fiction':
        books = Book.query.filter_by(genre='fiction').all()
    if filter_by == 'non-fiction':
        books = Book.query.filter_by(genre='non-fiction').all()
    if filter_by == 'horror':
        books = Book.query.filter_by(genre='horror').all()

    if filter_by == 'fysical':
        books = Book.query.filter_by(type='fysical').all()
    if filter_by == 'e-book':
        books = Book.query.filter_by(type='e-book').all()
    if filter_by == 'audio-book':
        books = Book.query.filter_by(type='audio-book').all()


    return render_template('general/home.html', books=books)


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)
