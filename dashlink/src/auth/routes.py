from src.auth import bp

@bp.route("/login")
def login():
    return "<h1>Login</h1>"

@bp.route("/logout")
def logout():
    return "<h1>Logout</h1>"

@bp.route("/sign-up")
def sign_up():
    return "<h1>Sign Up</h1>"
