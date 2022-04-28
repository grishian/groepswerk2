from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField


class LoginForm(FlaskForm):
    email = StringField('Email', id='login_email')
    password = PasswordField('Password', id='login_password')
    remember_me = BooleanField('Keep me logged in', id='remember_me')
    submit = SubmitField('Log In', id='login_submit')
