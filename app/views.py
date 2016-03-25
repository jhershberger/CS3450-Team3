from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
def index():
    return render_template("index.html")  # render the index template

@app.route('/profile')
def profile():
    user = {'username': 'Mcubed'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'username': 'John'}, 
            'body': 'What we do in the shadows is amazing!!' 
        },
        { 
            'author': {'username': 'Billy'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("profile.html",
                           title='Profile',
                           user=user,
                           posts=posts)

@app.route('/moviePage')
def moviePage():
    return render_template("moviePage.html")  # render the moviePage template

@app.route('/BasicSearchResults')
def BasicSearchResults():
    return render_template("BasicSearchResults.html")  # render the search results template

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
