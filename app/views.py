from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from imdbpie import Imdb
import random

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

imdb = Imdb()
imdb = Imdb(anonymize=True)
@app.route('/moviePage')
def moviePage():
        listOfPopularMovies = imdb.top_250()
        temp = random.randint(1, 249)
        t = listOfPopularMovies[temp]
        tid = t["tconst"]
        title = imdb.get_title_by_id(tid)
        year = t["year"]
        rating = t["rating"]
        actor = str(title.cast_summary[0].name)
        director = str(title.directors_summary[0].name)
        return render_template("moviePage.html", title=t["title"], year=year, rating=rating, actor=actor, director=director)  # render the moviePage template

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
