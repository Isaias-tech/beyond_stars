from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"placeholder": "example@email.com"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "*************"})
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    first_name = StringField(
        "First Name",
        validators=[
            DataRequired(message="First name is required."),
            Length(max=75, message="First name must be 75 characters or fewer."),
        ], render_kw={"placeholder": "Jhon..."}
    )
    last_name = StringField(
        "Last Name",
        validators=[
            DataRequired(message="Last name is required."),
            Length(max=150, message="Last name must be 150 characters or fewer."),
        ],render_kw={"placeholder": "Williams..."}
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required."),
            Email(message="Enter a valid email address."),
        ], render_kw={"placeholder": "example@email.com"}
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(min=8, max=128, message="Password must be between 8 and 128 characters."),
        ], render_kw={"placeholder": "**************"}
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Password confirmation is required."),
            EqualTo("password", message="Passwords must match."),
        ], render_kw={"placeholder": "**************"}
    )
    submit = SubmitField("Register")
