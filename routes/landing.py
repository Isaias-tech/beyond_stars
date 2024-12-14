from flask import render_template, Blueprint
from datetime import datetime


landing_bp = Blueprint("landing", __name__, url_prefix="/")


@landing_bp.app_context_processor
def set_context():
    return {"current_year": datetime.now().year}


@landing_bp.route("/")
def landing_page():
    return render_template("landing.html")
