from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user

from random import choices
from string import ascii_lowercase, digits
import json

from src.extensions import db
from src.main import bp
from src.models.link import Link
from src.main.forms import AddURL

BASE_URL = "dashlink.net"
AVAILABLE_CHARS = ascii_lowercase + digits

def generate_short_code():
    short_code = "".join(choices(AVAILABLE_CHARS, k=7))
    
    return "".join(short_code)

@bp.route("/", methods = ["GET", "POST"])
@login_required
def index():
    links = current_user.links
    
    form = AddURL()

    if form.validate_on_submit():
        link_clean = form.link.data.strip()

        is_valid_short_code = False
        while not is_valid_short_code:
            short_code = generate_short_code()

            existing_link = Link.query.filter(Link.short_code == short_code).first()

            if not existing_link:
                is_valid_short_code = True

        new_link = Link(
            short_code = short_code,
            short_link = f"{BASE_URL}/{short_code}",
            original_link = link_clean,
            creator_id = current_user.id
        )

        db.session.add(new_link)
        db.session.commit()

        flash("URL was added successfully!", category="success")

        return redirect(url_for("main.index"))
    
    else:
        for curr_error in form.errors:
            flash(form.errors[curr_error][0], category="error")

    return render_template("index.html", user=current_user, links=links, form=form)

@bp.route("/delete-link", methods = ["POST"])
@login_required
def delete_link():
    req = json.loads(request.data)
    link_id = int(req["linkId"])

    link = Link.query.get(link_id)

    if link:
        if link.creator_id == current_user.id:
            db.session.delete(link)
            db.session.commit()

    return jsonify({})

@bp.route("/<path>", methods = ["GET"])
def handle_redirect(path):
    # check to see if url path fits short_code format
    if path.isalnum() and (len(path) == 7):
        # check to see if a link with path as short code exists in db
        link = Link.query.filter(Link.short_code.ilike(path)).first()

        if link:
            return redirect(link.original_link)

    # any issues results in us sending the user back to the home page
    return redirect(url_for("main.index"))
