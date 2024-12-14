from flask import Flask


def init_blueprints(app: Flask):
    from routes.landing import landing_bp
    from routes.auth import auth_bp
    from routes.private import private_bp

    app.register_blueprint(landing_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(private_bp)
