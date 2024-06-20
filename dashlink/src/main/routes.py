from flask import render_template
from flask_login import login_required, current_user

from src.main import bp
from src.models.link import Link

@bp.route("/")
@login_required
def index():
    links = current_user.links

    return render_template("index.html", user=current_user, links=links)
