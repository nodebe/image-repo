from . import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String, nullable=False)
	pictures = db.relationship('Picture', backref='picture_poster')

class Picture(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	picture_name = db.Column(db.String, nullable=False)
	post_date = db.Column(db.DateTime)
	poster = db.Column(db.Integer, db.ForeignKey('user.id'))