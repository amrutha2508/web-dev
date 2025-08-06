import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # to give the image unique name 
    _, f_ext = os.path.splitext(form_picture.filename) # returns filename without extension, and extension
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user): # _external = True -> to get an absolute URL rather than relative URLs because the 
    token = user.get_reset_token() # relative URLs are fine within an application but link in the email needs to have full domain
    msg = Message('Password Reset Request', sender="amroot2508@gmail.com", recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: {url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)