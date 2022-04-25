from myapp.bp_book import bp_book
from flask import render_template


@bp_book.route('/book')
def do_book():
    return render_template('book/_book.html')
