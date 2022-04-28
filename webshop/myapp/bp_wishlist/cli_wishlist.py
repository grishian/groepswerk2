import click
from flask.cli import with_appcontext
from myapp import db
from myapp.bp_wishlist.model_wishlist import Wishlist
from myapp.bp_wishlist import bp_wishlist


@bp_wishlist.cli.command("create-wishlist_item")
@click.argument('user_id')
@click.argument('book_id')
@with_appcontext
def do_create_wishlist(user_id, book_id):
    wishlist = Wishlist()
    wishlist.user_id = user_id
    wishlist.book_id = book_id

    db.session.add(wishlist)
    db.session.commit()

