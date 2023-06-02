from app.main import main
from flask_login import login_required
from flask import render_template


@main.route('/')
def index():
    return 'This is the main blueprint'


@main.route('/dashboard')
# @login_required
def dashboard():
    return render_template('main/dashboard.html')
