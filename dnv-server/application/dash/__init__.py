import importlib

import dash

# list dash apps to be connected to flask app
dash_apps = ["demo1", "demo2"]

def dash_factory(server):
    """Dash app factory to connect apps to main flask server"""
    for app in dash_apps:
        dash_app = dash.Dash(server=server, routes_pathname_prefix=f"/{app}/")
        m = importlib.import_module(f"application.dash.{app}")
        dash_app.layout = m.create_layout()
        m.initialise_callbacks(dash_app)