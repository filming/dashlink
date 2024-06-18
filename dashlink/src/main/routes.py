from flask import render_template
from flask_login import login_required, current_user

from src.main import bp

@bp.route("/")
@login_required
def index():
    return render_template("index.html")
