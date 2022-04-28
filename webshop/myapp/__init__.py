from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager = LoginManager()

db = SQLAlchemy()

migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    app.debug = True

    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.session_protection = "basic"
    login_manager.login_view = 'do_login'

    do_register_blueprints(app)
    do_register_cli(app)

    migrate.init_app(app, db)
    return app

def do_register_blueprints(flaskapp):
    from myapp.bp_general import bp_general
    from myapp.bp_user import bp_user
    from myapp.bp_wishlist import bp_wishlist
    from myapp.bp_book import bp_book

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_user)
    flaskapp.register_blueprint(bp_wishlist)
    flaskapp.register_blueprint(bp_book)



def do_register_cli(flaskapp):
    from myapp.bp_general.utils_general import do_create_db
    from myapp.bp_user.cli_user import do_create_user
    from myapp.bp_book.cli_book import do_create_book

    flaskapp.cli.add_command(do_create_db)
    flaskapp.cli.add_command(do_create_user)
    flaskapp.cli.add_command(do_create_book)

