from flask import Flask

# MUST HAVE 2 underscores in file name __init__.py  2 before and 2 after


# Initializes flask - type this way
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ThE RaIn In SpAiN'

    # Imports from the connected files
    from .views import views
    from .auth import auth

    # Registers the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app
