from flask import Blueprint

bp_wishlist = Blueprint('bp_wishlist', __name__, cli_group="db")

from . import views_wishlist
