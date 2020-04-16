"""Routes for core Flask app."""
from flask import Blueprint, render_template, jsonify
from flask import current_app as app


main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    """Landing page."""
    return "This is blank because it shouldn't be accessed (yet)."


@main_bp.route('/status')
def status():
    return jsonify({'status': 'API OK'})