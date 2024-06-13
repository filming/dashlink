from flask import render_template

from src.auth import bp
from src.auth.forms import SignupForm

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/logout")
def logout():
    return "<h1>Logout</h1>"

@bp.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    form = SignupForm()

    if form.validate_on_submit():
        pass

    return render_template("auth/sign_up.html", form=form)
