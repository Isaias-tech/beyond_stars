from flask import render_template, Blueprint
from flask_login import login_required
from datetime import datetime


public_bp = Blueprint("public", __name__, url_prefix="/")


@public_bp.app_context_processor
def set_context():
    return {"current_year": datetime.now().year}


@public_bp.route("/overview")
def overview_page():
    return render_template("public/overview.html")


@public_bp.route("/checkout")
def checkout_page():
    return render_template("public/checkout.html")
