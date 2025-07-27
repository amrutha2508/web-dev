from flask import Flask, render_template

app = Flask(__name__) # __name__ is a special vairbale in python representing the name of the module

posts = [
    {
        'author':'trevor martin',
        'title': 'blog post 1',
        'content': 'first blog content',
        'date_posted': 'April 1, 2024'
    },
    {
        'author':'chelsea martin',
        'title': 'blog post 2',
        'content': 'group blog content',
        'date_posted': 'April 3, 2024'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title="About")
 



if __name__ == "__main__": 
    app.run(debug=True) # debug=True allows to view changes in the code by refreshing the webbrowser without rerunning the code in python
