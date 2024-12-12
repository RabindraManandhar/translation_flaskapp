from flask import Flask

def create_app():
    # Create and configure the Flask app
    app = Flask(__name__)

    # Import and register Blueprints here
    from . import translation
    app.register_blueprint(translation.bp)

    return app