from flask import render_template
from src.auth import bp

@bp.route("/login")
def login():
    return render_template("auth/login.html")

@bp.route("/logout")
def logout():
    return "<h1>Logout</h1>"

@bp.route("/sign-up")
def sign_up():
    return "<h1>Sign Up</h1>"
