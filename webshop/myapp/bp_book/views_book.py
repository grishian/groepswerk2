from myapp import db
from myapp.bp_book import bp_book
from myapp.bp_book.model_book import Book
from myapp.bp_book.form_book import BookForm
from myapp.bp_user.model_user import only_admins
from flask import render_template, redirect, url_for, flash


@bp_book.route('/book/<isbn>')
def do_book(isbn):

    book = Book.query.filter_by(isbn=isbn).first_or_404()

    return render_template('book/_book.html', book=book)


@bp_book.route('/add_book', methods=["GET", "POST"])
@only_admins
def add_book():

    form = BookForm()
    if form.validate_on_submit():
        book = Book()

        book.type = form.type.data
        book.title = form.title.data
        book.author = form.author.data
        book.isbn = form.isbn.data
        book.genre = form.genre.data
        book.price = form.price.data
        book.language = form.language.data
        book.series = form.series.data
        book.size = form.size.data
        book.size_type = form.size_type.data
        book.synopsis = form.synopsis.data
        book.cover = form.cover.data

        db.session.add(book)
        db.session.commit()

        flash('Book added.', 'OK')

        return redirect(url_for('bp_general.do_home'))

    return render_template('book/add_book.html', form=form)

