from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# MUST HAVE 2 underscores in file name __init__.py  2 before and 2 after

db = SQLAlchemy()
DB_NAME = 'database.db'

# Initializes flask - type this way


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ThE RaIn In SpAiN'
    app.config['SQLAlchemy_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Imports from the connected files
    from .views import views
    from .auth import auth

    # Registers the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # This sets up and loads the databases.  Must be after the blueprints etc.
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Checks for the path first then creates the database and sets it to itself setting up the database


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
