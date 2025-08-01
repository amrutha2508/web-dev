from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin # UserMixin is used to implement four functions for the User model; is_authenticated -> returns true if provided valid credentials, is_active, is_annonymous, get_id

@login_manager.user_loader #This tells Flask-Login how to retrieve a user object (typically from the database) given a user ID stored in the session cookie.
def load_user(user_id):
    return User.query.get(int(user_id)) 

# each class will be its own table in database
class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref="author", lazy=True) # by using 'Post' we are actually referencing Post class

    def __repr__(self): # how our object is printed __str__
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow) #datatime.utcnow - we want to pass the function as the argument not datetime.utcnow() which will assign same intial creation time for all the records
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False) # by using 'user' instead of User because we using 'user' table


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"