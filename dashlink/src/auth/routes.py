from flask import render_template, redirect, url_for

from src.auth import bp
from src.auth.forms import SignupForm, LoginForm

@bp.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

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
