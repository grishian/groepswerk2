from myapp.bp_book import bp_book
from myapp.bp_book.model_book import Book
from flask import render_template


@bp_book.route('/book/<isbn>')
def do_book(isbn):

    book = Book.query.filter_by(isbn=isbn).first_or_404()

    return render_template('book/_book.html', book=book)
