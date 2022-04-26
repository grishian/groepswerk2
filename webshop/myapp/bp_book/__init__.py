from flask import Blueprint

bp_book = Blueprint('bp_book', __name__, cli_group="db")

from . import views_book

