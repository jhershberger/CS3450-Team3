import flask
from flask import Flask, render_template, flash, redirect, url_for, request, Response
from app import app, login_manager
from .forms import LoginForm
from .models import User
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from imdbpie import Imdb
from random import randint
import webbrowser
import json
import requests
import random
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
login_manager.login_view = "login"

@app.route('/')
def index():
    return render_template("index.html")  # render the index template

@app.route('/baseUpdater', methods=['POST'])
def baseUpdater():
    global key
    global title
    # id = request.form['var']
    list250 = imdb.top_250()
    list10 = []
    newList10 = []
    besttitles = []
    print ("We're here")
    for x in range(0,10):
        rand = randint(0,249)
        list10.append(list250[rand])
    for x in range(0,10):
        newList10.append(list250[x])
    titles = []

    # print (list10)
    for item in list10:
        imdbid = item["tconst"]

        titles.append(item["title"])
    for item in newList10:
        besttitles.append(item["title"])


    return json.dumps({'status':'OK','title':titles,'besttitles':besttitles})

@app.route('/profile')
@login_required
def profile():
    user = current_user.id
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
    ids = []
    # directors= []
    print (list10)
    for item in list10:
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
        ids.append(imdbid)
        # print (newList10[x])

    return json.dumps({'status':'OK','list':newList10,'title':titles,'score':scores,'ids':ids})


@app.route('/movieUpdate',methods=['POST'])
def movieUpdate():
    global key

    imdbid = request.form['var']
    title = imdb.get_title_by_id(imdbid)

    #image stuff
    IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
    # print (KEY)
    r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=imdbid))
    api_response = r.json()

    rel_path = api_response['posters'][0]['file_path']
    url = "{0}{1}{2}".format(base_url, max_size, rel_path)

    year = title.year
    rating = title.rating
    actors = title.cast_summary
    names = ""
    for x in range(0, len(actors)):
        names += str(actors[x].name) + ", "

    genre = title.genres[0]
    runtime = int(title.runtime/60)
    plot = title.plot_outline
    director = str(title.directors_summary[0].name)
    print ("Almost")

    return render_template("moviePage.html", title=title.title, year=year, plot=plot, rating=rating,runtime=runtime, director=director, img=url, actor=names, genre=genre)

imdb = Imdb()
imdb = Imdb(anonymize=True)
@app.route('/moviePage')
def moviePage():
        global key
        listOfPopularMovies = imdb.top_250()
        temp = random.randint(1, 249)
        t = listOfPopularMovies[temp]
        imdbid = t["tconst"]
        title = imdb.get_title_by_id(imdbid)

        #image stuff
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
        # print (KEY)
        r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=imdbid))
        api_response = r.json()

        rel_path = api_response['posters'][0]['file_path']
        url = "{0}{1}{2}".format(base_url, max_size, rel_path)

        year = t["year"]
        rating = t["rating"]
        actors = title.cast_summary
        names = ""
        for x in range(0, len(actors)):
            names += str(actors[x].name) + ", "

        genre = title.genres[0]
        runtime = int(title.runtime/60)
        plot = title.plot_outline
        director = str(title.directors_summary[0].name)

        return render_template("moviePage.html", title=t["title"], year=year, plot=plot, rating=rating,runtime=runtime, director=director, img=url, actor=names, genre=genre)  # render the moviePage template

@app.route('/BasicSearchResults')
def BasicSearchResults():
    title = []
    year = []
    img = []
    sterm = imdb.search_for_title("The Dark Knight")
    print (sterm)
    for m in range (0,10):
        # imgtitle = imdb.get_title_by_id(sterm[m]["imdb_id"])
        # img.append(imgtitle.trailer_image_urls[0])
        # img.append(imgtitle.image["url"])
        # print (imdb.get_title_images(sterm[m]["imdb_id"]))
        title.append(sterm[m]["title"])
        year.append(sterm[m]["year"])
    return render_template("BasicSearchResults.html", img=img, title=title, year=year)  # render the search results template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            login_user(User(str(request.form['username']),str(request.form['password'])))
            return redirect(url_for('profile'))
    return render_template('login.html', error=error)

@app.route('/create')
def creation():
    return render_template('profCreation.html')


@login_manager.user_loader
def load_user(user_id):
    user = User('admin','admin')
    #get id from database
    #create instance of user of that id
    return user

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')
