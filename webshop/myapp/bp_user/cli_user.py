import click
from flask.cli import with_appcontext
from myapp import db
from myapp.bp_user.model_user import User
from myapp.bp_user import bp_user


@bp_user.cli.command("create-user")
@click.argument('email')
@click.argument('username')
@click.argument('password')
@with_appcontext
def do_create_user(email, username, password):
    user = User()
    user.email = email
    user.username = username
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
