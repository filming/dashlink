from flask import render_template, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash

from src.auth import bp
from src.auth.forms import SignupForm, LoginForm
from src.models.user import User
from src.extensions import db

@bp.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            return redirect(url_for('main.index'))

        return redirect(url_for('auth.login'))

    return render_template("auth/login.html", form=form)

@bp.route("/logout")
def logout():
    return "<h1>Logout</h1>"

@bp.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    form = SignupForm()

    if form.validate_on_submit():

        return redirect(url_for('auth.sign_up'))

    return render_template("auth/sign_up.html", form=form)
