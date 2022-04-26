from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    app.debug = True

    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    do_register_blueprints(app)

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