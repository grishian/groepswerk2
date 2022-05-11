from myapp import db


class Book(db.Model):
    __tablename__ = 'T_BOOK'

    type = db.Column('F_TYPE', db.String(50), nullable=False)
    title = db.Column('F_TITLE', db.String(300), nullable=False)
    author = db.Column('F_AUTHOR', db.String(50), nullable=False)
    isbn = db.Column('F_ISBN', db.String(13), nullable=False, primary_key=True, index=True)
    genre = db.Column('F_GENRE', db.String(50), nullable=False)
    price = db.Column('F_PRICE', db.String(15), nullable=True)
    language = db.Column('F_LANGUAGE', db.String(50), nullable=False)
    series = db.Column('F_SERIES', db.String (200), nullable=True)
    size = db.Column('F_SIZE', db.String(50), nullable=False)
    synopsis = db.Column('F_SYNOPSIS', db.String(5000))
    cover = db.Column('F_COVER', db.String(200))



    def __repr__(self):
        return '<Book_title: {}, Book_isbn: {}>'.format(self.title, self.isbn)
