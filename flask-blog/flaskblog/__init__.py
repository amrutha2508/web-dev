# intializes and ties together everything we need for our app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy is a class from flask_sqlalchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail



app = Flask(__name__) # __name__ is a special vairbale in python representing the name of the module

app.config['SECRET_KEY'] = '3258e93bd57939098b80c517d486336f' # generate this random key using import secrets, secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db" # the site.db will be created in the same folder as the present module

db = SQLAlchemy(app) # creating a database instance
# This app object is passed into SQLAlchemy(app) so the extension can:
# Read your database configuration from app.config
# Register itself with your app
# Set up the connection to your database
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Tells the extension where the login route is located, we passed the funciton name of the route 
login_manager.login_message_category = "info"
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# app.config['MAIL_USERNAME'] = 'enter your email'
# app.config['MAIL_PASSWORD'] = 'your_16_character_app_password'
mail = Mail(app) 

from flaskblog import routes