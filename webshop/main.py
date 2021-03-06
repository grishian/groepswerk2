import sys
from myapp import create_app, db
from myapp.bp_book.model_book import Book
from myapp.bp_user.model_user import User
from myapp.bp_wishlist.model_wishlist import Wishlist

sys.dont_write_bytecode = True

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Book': Book,
            'User': User,
            'Wishlist': Wishlist}


if __name__ == "__main__":
    app.run(debug=True)

