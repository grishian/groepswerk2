from myapp.bp_general import bp_general
from myapp.bp_book.model_book import Book
from flask import render_template, url_for



@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    books = Book.query.all()

    return render_template('general/home.html', books=books)
