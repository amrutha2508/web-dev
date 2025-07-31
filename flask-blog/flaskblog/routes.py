from flask import render_template, url_for, flash, redirect, request # request object to access query parameters
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
# Flask-Login makes current_user automatically available in all Jinja2 templates via a context processor.
# when you did login_manager = LoginManager(app), it registers a context processor behind the scenes like this:
# This tells Flask: “Make current_user available as a variable in every template.”
# @app.context_processor
# def _user_context_processor():
#     return dict(current_user=current_user)

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
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About Page")

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()     # A RegistrationForm() is created and rendered.
    if form.validate_on_submit(): # it checks request.method == "POST" and form.validate() == True
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to login!','success')# 'success' - type of bootstrap class you want the alert to have
        return redirect(url_for('login')) # home - name of the function for that route
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data): # if user exists and password is valid with that in database
            login_user(user, remember = form.remember.data) # log the user in
            next_page = request.args.get('next') # returns none if next parameter doesn't exist
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessfull. Please check email and password','danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required # Tells the extension that we need to login to access the account route
def account():
    return render_template('account.html',title="Account")

