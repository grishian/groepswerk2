from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField


class LoginForm(FlaskForm):
    email = StringField('Email', id='login_email')
    password = PasswordField('Password', id='login_password')
    remember_me = BooleanField('Keep me logged in', id='remember_me')
    submit = SubmitField('Log In', id='login_submit')


class SignUpForm(FlaskForm):
    email = StringField('Email', id='signup_email')
    username = StringField('Username', id='signup_username')
    password = PasswordField('Password', id='signup_password')
    submit = SubmitField('Submit', id='signup_submit')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', id='change_password_old')
    new_password = PasswordField('New password', id='change_password_new')
    repeat_password= PasswordField('Repeat password', id='change_password_new2')
    submit = SubmitField('Change password', id='change_password_submit')

