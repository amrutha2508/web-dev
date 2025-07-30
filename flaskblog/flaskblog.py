from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy is a class from flask_sqlalchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__) # __name__ is a special vairbale in python representing the name of the module

app.config['SECRET_KEY'] = '3258e93bd57939098b80c517d486336f' # generate this random key using import secrets, secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db" # the site.db will be created in the same folder as the present module

db = SQLAlchemy(app) # creating a database instance
# This app object is passed into SQLAlchemy(app) so the extension can:
# Read your database configuration from app.config
# Register itself with your app
# Set up the connection to your database

# each class will be its own table in database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref="author", lazy=True) # by using 'Post' we are actually referencing Post class

    def __repr__(self): # how our object is printed __str__
        return f"User('{self.username}','{self.email}','{self.image_file}')"U
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow) #datatime.utcnow - we want to pass the function as the argument not datetime.utcnow() which will assign same intial creation time for all the records
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False) # by using 'user' instead of User because we using 'user' table


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

posts = [
    {
        'author':'raj',
        'title':'blog post1',
        'content':'content1',
        'date_posted':'April 20, 2018'
    },
    {
        'author':'rekha',
        'title':'blog post3',
        'content':'content by rekha',
        'date_posted':'April 21, 2018'
    }
]

@app.route("/") 
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About Page")

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()     # A RegistrationForm() is created and rendered.
    if form.validate_on_submit(): # it checks request.method == "POST" and form.validate() == True
        flash(f'Account created for {form.username.data}!','success') # 'success' - type of bootstrap class you want the alert to have
        return redirect(url_for('home')) # home - name of the function for that route
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash(f'You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessfull. Please check email and password','danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)


