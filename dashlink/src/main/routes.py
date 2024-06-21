from flask import render_template
from flask_login import login_required, current_user

from random import choices
from string import ascii_lowercase, digits

from src.extensions import db
from src.main import bp
from src.models.link import Link
from src.main.forms import AddURL

BASE_URL = "dashlink.net"
AVAILABLE_CHARS = ascii_lowercase + digits

def generate_short_code():
    short_code = "".join(choices(AVAILABLE_CHARS, k=7))
    
    return "".join(short_code)

@bp.route("/")
@login_required
def index():
    links = current_user.links

    return render_template("index.html", user=current_user, links=links)
