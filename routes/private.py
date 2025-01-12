from flask import render_template, Blueprint
from flask_login import login_required
from datetime import datetime


private_bp = Blueprint("private", __name__, url_prefix="/")


@private_bp.app_context_processor
def set_context():
    return {"current_year": datetime.now().year}


@private_bp.route("/home")
@login_required
def home_page():
    return render_template("private/home.html")

@private_bp.route("/profile")
@login_required
def profile_page():
    return render_template("private/profile.html")
