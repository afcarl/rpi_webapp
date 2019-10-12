"""The app module, containing the app factory function."""
import logging
import sys
import os

from flask import Flask, render_template

from rpi_webapp import data

def create_app():
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    """
    app = Flask(__name__.split('.')[0])

    # Use default settings then overide with settings file
    # contained in environment variable SETTINGS
    app.config.from_object('rpi_webapp.default_settings')

    if 'SETTINGS' in os.environ:
        app.config.from_envvar('SETTINGS')

    register_blueprints(app)
    return app

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(data.views.blueprint)
