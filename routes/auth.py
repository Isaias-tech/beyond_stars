from controllers.user_controllers import register_controller, login_controller
from flask import render_template, Blueprint, flash, redirect, url_for
from forms.user_forms import LoginForm, RegisterForm
from flask_login import logout_user, login_required

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        data = {"email": form.email.data, "password": form.password.data}

        return login_controller(data, form)

    if form.errors:
        for field, error_list in form.errors.items():
            for error in error_list:
                flash(f"{field}: {error}", "error")

    return render_template("auth/login.html", form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data

        return register_controller(data, form)

    if form.errors:
        for field, error_list in form.errors.items():
            for error in error_list:
                flash(f"{field}: {error}", "error")

    return render_template("auth/register.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("landing.landing_page"))
