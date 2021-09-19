import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from image_repo.main.routes import main

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'cbfGRKJmgtmUQTmtfZDCtZwXlfFdhcjkIVdoWcvJBpAUQkXXjc'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') or 'sqlite:///image_repo.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager =  LoginManager(app)
login_manager.login_view = 'main.login'

app.register_blueprint(main)


db.create_all()
db.session.commit()