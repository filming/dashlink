from flask import render_template, redirect, url_for, flash

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

        if user:
            if check_password_hash(user.password, form.password.data):
                flash("Logged in successfully!", category="success")
                return redirect(url_for('main.index'))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("User does not exist!", category="error")

        return redirect(url_for('auth.login'))

    return render_template("auth/login.html", form=form)

@bp.route("/logout")
def logout():
    return "<h1>Logout</h1>"

@bp.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    form = SignupForm()

    if form.validate_on_submit():
        new_user = User(
            username = form.username.data,
            email = form.email.data,
            password = generate_password_hash(form.password.data)
        )
        
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template("auth/sign_up.html", form=form)
