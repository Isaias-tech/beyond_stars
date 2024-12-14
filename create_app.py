from extensions import db, ma, migrate, bcrypt, login_manager
from routes.init_blueprints import init_blueprints
from dotenv import load_dotenv
from models.user import User
from flask import Flask
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
env_file = os.path.join(BASE_DIR, ".env")

if os.path.exists(env_file):
    load_dotenv(env_file)


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "In$e(ur3-$3(r37-k3y"),
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URI", f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    app.name = "Beyond Stars"

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login_page"
    login_manager.login_message = "You need to log in to access this page."

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    init_blueprints(app)

    return app
