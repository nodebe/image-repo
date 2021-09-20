from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from image_repo.main.forms import InsertImageForm, LoginForm
from image_repo.main.utils import save_picture
from image_repo.models import User, Picture
from image_repo import db
from passlib.hash import sha256_crypt as sha256
from datetime import datetime as dt

main = Blueprint('main', __name__)

@main.route('/')
def index():
	file_form = InsertImageForm()
	login_form = LoginForm()
	return render_template('index.html', file_form=file_form, login_form=login_form)

@main.route('/login', methods=["POST"])
def login():
	login_form = LoginForm()
	try:
		hashed_password = sha256.encrypt(str(login_form.password.data))
		if login_form.validate_on_submit():
			user = User.query.filter_by(email=login_form.email.data).first()
		if user:
			if sha256.verify(login_form.password.data, user.password):
				login_user(user)
				return redirect(url_for('main.index'))
			else:
				flash('Password is incorrect.', 'warning')
				return render_template('index.html')
		else: # If user does not exist in database, create an account for user and login. Would normally do an email verification here...
			user = User(email=email,password=hashed_password)
			db.session.add(user)
	except Exception as e:
		flash(f'Something went wrong: {e}', 'warning')
	else:
		db.session.commit()
		login_user(user)
	return redirect(url_for('main.index'))

@main.route('/dashboard')
def dashboard():
	login_form = LoginForm()
	file_form = InsertImageForm()
	return render_template('dashboard.html', login_form=login_form, file_form=file_form)

@main.route('/filespostform', methods=["POST"])
def filespostform():
	file_form = InsertImageForm()
	try:
		if file_form.validate_on_submit() and file_form.file.data:
			pictures = save_picture(file_form.file.data)
			for picture in pictures:
				new_picture = Picture(picture_name=picture,post_date=dt.now(),poster=current_user.id)
				db.session.add(new_picture)
		else:	
			flash('Please select one or more images', 'warning')
	except Exception as e:
		print(f'{e}')
	else:
		db.session.commit()
		flash('Your images have been added.', 'success')

	return redirect(url_for('main.dashboard'))

@main.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.index'))