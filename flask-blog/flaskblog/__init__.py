# intializes and ties together everything we need for our app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy is a class from flask_sqlalchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy() # creating a database instance
# This app object is passed into SQLAlchemy(app) so the extension can:
# Read your database configuration from app.config
# Register itself with your app
# Set up the connection to your database
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' # Tells the extension where the login route is located, we passed the funciton name of the route 
login_manager.login_message_category = "info"
mail = Mail() 

def create_app(config_class=Config):
    app = Flask(__name__) # __name__ is a special vairbale in python representing the name of the module
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app) 

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app

    

