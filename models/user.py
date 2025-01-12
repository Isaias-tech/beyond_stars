from datetime import datetime, timezone
from extensions import db, bcrypt
from flask_login import UserMixin
import sqlalchemy as sa


class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String(75))
    last_name = sa.Column(sa.String(150))
    email = sa.Column(sa.String(), unique=True)
    password = sa.Column(sa.String(128))
    phone_number = sa.Column(sa.String(21))
    first_address = sa.Column(sa.Text())
    second_address = sa.Column(sa.Text())
    zip_code = sa.Column(sa.String(10))
    created_at = sa.Column(sa.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = sa.Column(
        sa.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    is_admin = sa.Column(sa.Boolean(), default=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
