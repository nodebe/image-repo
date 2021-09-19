from flask_wtf import FlaskForm
from wtforms import PasswordField, FileField, MultipleFileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed

class InsertImageForm(FlaskForm):
	file = MultipleFileField('File', validators=[FileAllowed(['jpg','JPG','png','PNG']), InputRequired()])

class LoginForm(FlaskForm):
	email = EmailField('', validators=[InputRequired()])
	password = PasswordField('', validators=[InputRequired()])