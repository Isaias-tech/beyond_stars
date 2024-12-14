from schemas.user_schemas import RegisterSchema, LoginSchema
from flask import flash, render_template, redirect, url_for
from forms.user_forms import RegisterForm, LoginForm
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_user
from models.user import User
from create_app import db


def login_controller(data: dict, form: LoginForm):
    schema = LoginSchema()
    errors = schema.validate(data)

    if errors:
        for field, error_list in errors.items():
            for error in error_list:
                flash(f"{field}: {error}", "error")
        return render_template("auth/login.html", form=form)

    user = User.query.filter_by(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        flash("Invalid email or password.", "error")
        return render_template("auth/login.html", form=form)

    login_user(user)
    flash("Login successful!", "success")
    return redirect(url_for("private.home_page"))


def register_controller(data: dict, form: RegisterForm):
    schema = RegisterSchema()
    errors = schema.validate(data)

    if errors:
        for field, error_list in errors.items():
            for error in error_list:
                flash(f"{field}: {error}", "error")
        return render_template("auth/register.html", form=form)

    if User.query.filter_by(email=data["email"]).first():
        flash(f"Email already registered", "error")
        return render_template("auth/register.html", form=form)

    try:
        user = User(first_name=data.get("first_name"), last_name=data.get("last_name"), email=data.get("email"))
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()

        return redirect("/home")
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f"Server error", "error")
        return render_template("auth/register.html", form=form)
