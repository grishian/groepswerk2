import click
from flask.cli import with_appcontext
from myapp import db
from myapp.bp_book.model_book import Book
from myapp.bp_book import bp_book

@bp_book.cli.command("create-book")
@click.argument('F_TYPE')
@click.argument('F_TITLE')
@click.argument('F_AUTHOR')
@click.argument('F_ISBN')
@click.argument('F_GENRE')
@click.argument('F_PRICE')
@click.argument('F_LANGUAGE')
@click.argument('F_SERIES')
@click.argument('F_SIZE')
@click.argument('F_SYNOPSIS')
@click.argument('F_COVER')
@with_appcontext
def do_create_book(type, title, author, isbn, genre, price, language, series, size, synopsis, cover):
    book = Book()
    book.type = type
    book.title = title
    book.author = author
    book.isbn = isbn
    book.genre = genre
    book.price = price
    book.language = language
    book.series = series
    book.size = size
    book.synopsis = synopsis
    book.cover = cover
    db.session.add(book)
    db.session.commit()
