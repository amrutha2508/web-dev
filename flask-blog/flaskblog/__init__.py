# intializes and ties together everything we need for our app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy is a class from flask_sqlalchemy



app = Flask(__name__) # __name__ is a special vairbale in python representing the name of the module

app.config['SECRET_KEY'] = '3258e93bd57939098b80c517d486336f' # generate this random key using import secrets, secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db" # the site.db will be created in the same folder as the present module

db = SQLAlchemy(app) # creating a database instance
# This app object is passed into SQLAlchemy(app) so the extension can:
# Read your database configuration from app.config
# Register itself with your app
# Set up the connection to your database

from flaskblog import routes