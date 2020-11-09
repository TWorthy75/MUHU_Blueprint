from flask import Flask
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_bp)

        return app
        



