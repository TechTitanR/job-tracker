from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate  # <-- Required for migrations
from config import Config

db = SQLAlchemy()
migrate = Migrate()  # <-- Required
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # <-- Required for 'flask db' commands
    login_manager.init_app(app)
    mail.init_app(app)

    from .routes import main
    from .auth_routes import auth
    from .scheduler import start_scheduler  # ✅ clean import here

    app.register_blueprint(main)
    app.register_blueprint(auth)

    start_scheduler(app)   # ✅ start background APScheduler

    return app
