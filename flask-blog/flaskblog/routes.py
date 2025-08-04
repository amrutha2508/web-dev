import secrets, os
from PIL import Image # from Pillow package
from flask import render_template, url_for, flash, redirect, request, abort # request object to access query parameters
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
# Flask-Login makes current_user automatically available in all Jinja2 templates via a context processor.
# when you did login_manager = LoginManager(app), it registers a context processor behind the scenes like this:
# This tells Flask: “Make current_user available as a variable in every template.”
# @app.context_processor
# def _user_context_processor():
#     return dict(current_user=current_user)


@app.route("/") 
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    # posts = Post.query.paginate(page=page, per_page=5)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # to give the image unique name 
    _, f_ext = os.path.splitext(form_picture.filename) # returns filename without extension, and extension
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route('/account',methods=['GET','POST'])
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
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename="profile_pics/"+current_user.image_file)
    return render_template('account.html',title="Account",image_file=image_file, form=form)

@app.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content = form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title="New Post", form=form, legend="New Post")

@app.route('/post/<int:post_id>') # adding variables(id of the post) in the route
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/post/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!','success')
        return redirect(url_for('post',post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title="Update Post", form=form, legend="Update Post")

@app.route('/post/<int:post_id>/delete',methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!','success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('user_post.html', posts = posts, user=user)

def send_reset_email(user): # _external = True -> to get an absolute URL rather than relative URLs because the 
    token = user.get_reset_token() # relative URLs are fine within an application but link in the email needs to have full domain
    msg = Message('Password Reset Request', sender="amroot2508@gmail.com", recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: {url_for('reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@app.route("/reset_password",methods=['GET','POST']) # route to put in email to send info to change password
def reset_request(): 
    if current_user.is_authenticated: # we want the user to be loged out to use this
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset the password.','info')
        return redirect(url_for('login'))
    return render_template('reset_request.html',title="Reset Password",form=form)


@app.route('/reset_password/<token>',methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token','warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit(): # it checks request.method == "POST" and form.validate() == True
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated! You are now able to login!','success')# 'success' - type of bootstrap class you want the alert to have
        return redirect(url_for('login'))
    return render_template('reset_token.html',title='Reset Password', form=form)



