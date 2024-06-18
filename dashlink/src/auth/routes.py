from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from werkzeug.security import generate_password_hash, check_password_hash

from src.auth import bp
from src.auth.forms import SignupForm, LoginForm
from src.models.user import User
from src.extensions import db

@bp.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username.ilike(form.username.data)).first()

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                flash("Logged in successfully!", category="success")

                return redirect(url_for('main.index'))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("User does not exist!", category="error")

        return redirect(url_for('auth.login'))
    
    else:
        for curr_error in form.errors:
            flash(form.errors[curr_error][0], category="error")

    return render_template("auth/login.html", form=form, user=current_user)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

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

        login_user(new_user, remember=True)

        flash("Account created successfully!", category="success")

        return redirect(url_for('main.index'))
    
    else:
        for curr_error in form.errors:
            flash(form.errors[curr_error][0], category="error")

    return render_template("auth/sign_up.html", form=form, user=current_user)
