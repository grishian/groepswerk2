from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class BookForm(FlaskForm):

    type = StringField('Type', id='book_type')
    title = StringField('Title', id='book_title')
    author = StringField('Author', id='book_author')
    isbn = StringField('Isbn', id='book_isbn')
    genre = StringField('Genre', id='book_genre')
    price = StringField('Price', id='book_price')
    language = StringField('Language', id='book_language')
    series = StringField('Series', id='book_series')
    size = StringField('Size', id='book_size')
    synopsis = TextAreaField('Synopsis', id='book_synopsis')
    cover = StringField('Cover url', id='book_cover')
    submit = SubmitField('Add book', id='book_add')

