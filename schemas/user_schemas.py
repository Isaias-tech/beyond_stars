from marshmallow import Schema, fields, validate, ValidationError, validates_schema, EXCLUDE
from models.user import User
from create_app import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=8))


class LoginSchema(Schema):
    email = fields.Email(required=True, validate=validate.Email())
    password = fields.String(required=True, validate=validate.Length(min=8))

    class Meta:
        unknown = EXCLUDE


class RegisterSchema(Schema):
    first_name = fields.Str(
        required=True,
        validate=validate.Length(max=75, error="First name must be 75 characters or fewer."),
    )
    last_name = fields.Str(
        required=True,
        validate=validate.Length(max=150, error="Last name must be 150 characters or fewer."),
    )
    email = fields.Email(required=True, validate=validate.Email(error="Enter a valid email address."))
    password = fields.Str(
        required=True,
        validate=validate.Length(min=8, max=128, error="Password must be between 8 and 128 characters."),
    )
    confirm_password = fields.Str(required=True)

    @validates_schema
    def validate_passwords(self, data, **kwargs):
        if data["password"] != data["confirm_password"]:
            raise ValidationError({"confirm_password": "Passwords must match."})

    class Meta:
        unknown = EXCLUDE
