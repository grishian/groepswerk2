from myapp.bp_general import bp_general
from myapp.bp_book.model_book import Book
from flask import render_template, url_for, redirect, request


@bp_general.route('/', methods=['GET', 'POST'])
@bp_general.route('/index', methods=['GET', 'POST'])
def do_home():
    """
    Display all books, using pagination.
    When search is used: only display searched books.
    :return: 'all books(pagination)' or 'searched books'
    """
    all_books = Book.query.all()
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page, 3, False)
    next_url = url_for('bp_general.do_home', page=books.next_num) \
        if books.has_next else None
    prev_url = url_for('bp_general.do_home', page=books.prev_num) \
        if books.has_prev else None
    books = books.items

    if request.method == 'POST':

        items = request.form.getlist('slim_select')

        books = []

        for isbn in items:
            books.append(Book.query.filter_by(isbn=isbn).first())

        if items is None:
            return redirect('/')
        # when empty : method not allowed
    return render_template('general/home.html', books=books, next_url=next_url, prev_url=prev_url,
                           all_books=all_books)


@bp_general.route('/filter/<filter_by>', methods=['POST', 'GET'])
def do_filter(filter_by):
    """
    Order and filter function.
    :param filter_by: filter or order method.
    :return: homepage with filtered or ordered books
    """
    all_books = Book.query.all()
    page = request.args.get('page', 1, type=int)

    if filter_by == 'alphabetic':
        books = Book.query.order_by(Book.title).paginate(page, 3, False)
    if filter_by == 'price_desc':
        books = Book.query.order_by(Book.price.desc()).paginate(page, 3, False)
    if filter_by == 'price_asc':
        books = Book.query.order_by(Book.price.asc()).paginate(page, 3, False)

    if filter_by == 'Action':
        books = Book.query.filter_by(genre='Action').paginate(page, 3, False)
    if filter_by == 'Adventure':
        books = Book.query.filter_by(genre='Adventure').paginate(page, 3, False)
    if filter_by == 'Comic':
        books = Book.query.filter_by(genre='Comic').paginate(page, 3, False)
    if filter_by == 'Detective':
        books = Book.query.filter_by(genre='Detective').paginate(page, 3, False)
    if filter_by == 'Fantasy':
        books = Book.query.filter_by(genre='Fantasy').paginate(page, 3, False)
    if filter_by == 'History':
        books = Book.query.filter_by(genre='History').paginate(page, 3, False)
    if filter_by == 'Horror':
        books = Book.query.filter_by(genre='Horror').paginate(page, 3, False)
    if filter_by == 'Informative':
        books = Book.query.filter_by(genre='Informative').paginate(page, 3, False)
    if filter_by == 'Non-fiction':
        books = Book.query.filter_by(genre='Non-fiction').paginate(page, 3, False)
    if filter_by == 'Poetry':
        books = Book.query.filter_by(genre='Poetry').paginate(page, 3, False)
    if filter_by == 'Romance':
        books = Book.query.filter_by(genre='Romance').paginate(page, 3, False)
    if filter_by == 'Science Fiction (Sci-Fi)':
        books = Book.query.filter_by(genre='Science Fiction (Sci-Fi)').paginate(page, 3, False)
    if filter_by == 'Thriller':
        books = Book.query.filter_by(genre='Thriller').paginate(page, 3, False)

    if filter_by == 'Physical book':
        books = Book.query.filter_by(type='Physical book').paginate(page, 3, False)
    if filter_by == 'E-book':
        books = Book.query.filter_by(type='E-book').paginate(page, 3, False)
    if filter_by == 'Audiobook':
        books = Book.query.filter_by(type='Audiobook').paginate(page, 3, False)

    next_url = url_for('bp_general.do_home', page=books.next_num) \
        if books.has_next else None
    prev_url = url_for('bp_general.do_home', page=books.prev_num) \
        if books.has_prev else None

    return render_template('general/home.html', books=books.items, next_url=next_url, prev_url=prev_url,
                           all_books=all_books)


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)
