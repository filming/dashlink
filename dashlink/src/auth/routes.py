from src.auth import bp

@bp.route("/login")
def login():
    return "<h1>Login</p>"
