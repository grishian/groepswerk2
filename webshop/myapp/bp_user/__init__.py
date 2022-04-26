from flask import Blueprint

bp_user = Blueprint('bp_user', __name__, cli_group="db")

from . import views_user