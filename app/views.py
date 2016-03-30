from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from imdbpie import Imdb
from random import randint
import webbrowser
import json
import requests
imdb = Imdb()
imdb = Imdb(anonymize = True)
imdb = Imdb(cache=True)
global KEY
KEY = '90a0a4c3608d4231153c2915f1806c39'
CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
url = CONFIG_PATTERN.format(key=KEY)
r = requests.get(url)
config = r.json()
base_url = 'https://image.tmdb.org/t/p/'
max_size = 'original'

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

@app.route('/testSERVER', methods=['POST'])
def testSERVER():
    global key
    print("hello")
    global title
    # id = request.form['var']
    list250 = imdb.top_250()
    list10 = []
    newList10 = []

    for x in range(0,10):
        rand = randint(0,249)
        list10.append(list250[rand])

    # temp = imdb.get_title_by_id(id)
    # print (temp.poster_url)
    titles = []
    scores = []
    # directors= []
    print (list10)
    for item in list10:
        print("hello")
        # webbrowser.open(list10[x]["image"]["url"])
        # webbrowser.close(list10[x]["image"]["url"])
        # print (list10[x])
        imdbid = item["tconst"]
        # title = imdb.get_title_by_id(imdbid)
        # print (imdbid)
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
        # print (KEY)
        r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=imdbid))
        api_response = r.json()

        rel_path = api_response['posters'][0]['file_path']
        # print (posters)
        poster_urls= []
        url = "{0}{1}{2}".format(base_url, max_size, rel_path)
        poster_urls.append(url)
        newList10.append(poster_urls)
        scores.append(item["rating"])
        # directors.append(title.directors_summary[0].name)
        titles.append(item["title"])
        # print (newList10[x])

    return json.dumps({'status':'OK','list':newList10,'title':titles,'score':scores})


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
