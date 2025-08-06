import os

class Config:
    SECRET_KEY = '3258e93bd57939098b80c517d486336f' # generate this random key using import secrets, secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db" # the site.db will be created in the same folder as the present module
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'amroot2508@gmail.com'
    MAIL_PASSWORD = 'oumc pgit gcnn jigd'