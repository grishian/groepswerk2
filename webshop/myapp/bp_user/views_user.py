import logging
from flask import render_template, abort, flash, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from myapp import db
from myapp.bp_user import bp_user
from myapp.bp_user.model_user import User, only_admins
from myapp.bp_user.form_user import LoginForm, SignUpForm


@bp_user.route('/user')
def do_user():
    return render_template('user/user.html')



@bp_user.route("/login", methods=["GET", "POST"])
def do_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if not user.check_password(form.password.data):
                flash('Wrong password', 'WARNING')
            else:
                # in case we have another user still logged in
                if current_user and current_user.is_authenticated:
                    try:
                        current_user.authenticated = False
                        db.session.add(current_user)
                        db.session.commit()
                        logout_user()
                    except Exception as e:   # pragma: no cover
                        # if this fails we do not care, but we certainly do not want to block
                        # someone logging in
                        logging.info('Error during login (logout): {}'.format(e))

                # now set the new user to authenticated
                user.authenticated = True
                db.session.add(user)
                db.session.commit()

                # do the actual login
                login_user(user, remember=form.remember_me.data)

                flash('You are now logged in', 'OK')


                return redirect(url_for('bp_general.do_home'))
        else:
            flash('Wrong email or password', 'WARNING')

    return render_template('user/login.html', form=form)


@bp_user.route("/logout", methods=["GET"])
@login_required
def do_logout():
    user = current_user
    if user and user.is_authenticated:
        user.authenticated = False
        db.session.add(user)
        db.session.commit()
        flash('You are now logged out', 'OK')
        logout_user()
        return redirect(url_for('bp_general.do_home'))


@bp_user.route('/register', methods=['GET', 'POST'])
def do_register():
    user = current_user
    if user and user.is_authenticated:
        flash('You are already logged in, you can not signup', 'WARNING')
        return redirect(url_for('bp_general.do_home'))

    form = SignUpForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        user.profile_type = 1
        user.active = True

        db.session.add(user)
        db.session.commit()

        flash('You are successfully registered.', 'OK')
        return redirect(url_for('bp_user.do_login', user_id=user.id))

    return render_template('user/register.html', form=form)
