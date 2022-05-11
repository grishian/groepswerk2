from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, HiddenField


class BookForm(FlaskForm):

    type = SelectField('Type', choices=[('No type specified', 'Please select a book type'),
                                        ('Physical book', 'Physical book'),
                                        ('E-book', 'E-book'),
                                        ('Audiobook', 'Audiobook')])
    title = StringField('Title', id='book_title')
    author = StringField('Author', id='book_author')
    isbn = StringField('Isbn', id='book_isbn')
    genre = SelectField('Genre', choices=[('No genre specified', 'Please select a genre'),
                                         ('Action', 'Action'),
                                         ('Adventure', 'Adventure'),
                                         ('Comic', 'Comic'),
                                         ('Detective', 'Detective'),
                                         ('Fantasy', 'Fantasy'),
                                         ('History', 'History'),
                                         ('Horror', 'Horror'),
                                         ('Informative', 'Informative'),
                                         ('Non-fiction', 'Non-fiction'),
                                         ('Poetry', 'Poetry'),
                                         ('Romance', 'Romance'),
                                         ('Science Fiction (Sci-Fi)', 'Science Fiction (Sci-Fi)'),
                                         ('Thriller', 'Thriller')])
    price = StringField('Price', id='book_price')
    language = StringField('Language', id='book_language')
    series = StringField('Series', id='book_series')
    size = StringField('Size', id='book_size')
    size_type = SelectField('Size type', choices=[(0, 'Please select a size type'),
                                         ('Pages', 'Pages'),
                                         ('Minutes', 'Minutes'),
                                         ('Characters', 'Characters'),
                                         ('Mb', 'Mb')])
    synopsis = TextAreaField('Synopsis', id='book_synopsis')
    cover = StringField('Cover url', id='book_cover')
    submit = SubmitField('Submit', id='book_add')


