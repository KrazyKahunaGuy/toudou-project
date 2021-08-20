from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_seasurf import SeaSurf

from .config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = SeaSurf()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    from toudou.todo import todo
    app.register_blueprint(todo)

    from toudou.pages import pages
    app.register_blueprint(pages)

    from toudou.auth import auth
    app.register_blueprint(auth)

    return app


app = create_app()
app.app_context().push()
