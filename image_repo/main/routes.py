from flask import Blueprint, render_template
from flask_login import current_user, login_user, login_required, logout_user
from image_repo.main.forms import InsertImageForm
from datetime import datetime as dt

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/login')
def login():
	return render_template('login.html')

@main.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.index'))