from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # __name__ is a special vairbale in python representing the name of the module

app.config['SECRET_KEY'] = '3258e93bd57939098b80c517d486336f' # generate this random key using import secrets, secrets.token_hex(16)

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
    app.run(debug=True)


