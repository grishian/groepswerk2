from myapp import db


class Wishlist(db.Model):
    __tablename__ = 'T_WISHLIST'

    id = db.Column('F_ID', db.Integer, nullable=False, primary_key=True, index=True)
    user_id = db.Column('F_USER_ID', db.Integer, nullable=False)
    book_id = db.Column('F_BOOK_ID', db.String(13), nullable=False)



