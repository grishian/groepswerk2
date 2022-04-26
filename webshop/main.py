import sys
from myapp import create_app, db
from myapp.bp_book.model_book import Book

sys.dont_write_bytecode = True

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Book': Book}


if __name__ == "__main__":
    app.run(debug=True)

