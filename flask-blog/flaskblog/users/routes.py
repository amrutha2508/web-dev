from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email


users = Blueprint('users',__name__) #'users' is name of the blue print

@users.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main/home'))
    form = RegistrationForm()     # A RegistrationForm() is created and rendered.
    if form.validate_on_submit(): # it checks request.method == "POST" and form.validate() == True
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to login!','success')# 'success' - type of bootstrap class you want the alert to have
        return redirect(url_for('users.login')) # home - name of the function for that route
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data): # if user exists and password is valid with that in database
            login_user(user, remember = form.remember.data) # log the user in
            next_page = request.args.get('next') # returns none if next parameter doesn't exist
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Login Unsuccessfull. Please check email and password','danger')
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route('/account',methods=['GET','POST'])
@login_required # Tells the extension that we need to login to access the account route
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!','success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename="profile_pics/"+current_user.image_file)
    return render_template('account.html',title="Account",image_file=image_file, form=form)

@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('user_post.html', posts = posts, user=user)

@users.route("/reset_password",methods=['GET','POST']) # route to put in email to send info to change password
def reset_request(): 
    if current_user.is_authenticated: # we want the user to be loged out to use this
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset the password.','info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html',title="Reset Password",form=form)


@users.route('/reset_password/<token>',methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token','warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit(): # it checks request.method == "POST" and form.validate() == True
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated! You are now able to login!','success')# 'success' - type of bootstrap class you want the alert to have
        return redirect(url_for('users.login'))
    return render_template('reset_token.html',title='Reset Password', form=form)