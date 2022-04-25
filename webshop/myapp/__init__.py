from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    app.debug = True
    #configuration

    do_register_blueprints(app)

    return app

def do_register_blueprints(flaskapp):
    from myapp.bp_general import bp_general
    from myapp.bp_user import bp_user

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_user)