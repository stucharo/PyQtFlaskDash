"""Initialize app."""
from flask import Flask

def create_app():
    """Construct the core application."""
    app = Flask(__name__)

    with app.app_context():

        # Import main Blueprint
        from application import routes
        app.register_blueprint(routes.main_bp)

        # Import Dash application
        from application.dash.demo import Add_Demo1, Add_Demo2
        app = Add_Demo1(app)
        app = Add_Demo2(app)

        return app