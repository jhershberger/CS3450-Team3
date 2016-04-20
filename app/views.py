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

# load the adapter
import psycopg2

# load the psycopg extras module
import psycopg2.extras

from .methods import methods as _m

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
    # try:
    #     conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
    #     print("Successful connection to the database!")
    # except:
    #     print("I am unable to connect to the database")

    # cur = conn.cursor()
    # user = current_user.first_name
    user = str(User.instances[0].first_name) + " " + str(User.instances[0].last_name)
    email = str(User.instances[0].email)
    username = str(User.instances[0].username)
    friendCount = _m.queryFriendCount(User.instances[0].id)
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
                           email=email,
                           username=username,
                           friendCount=friendCount,
                           posts=posts,
                           currentUser = True)

@app.route('/friendsProfile')
@login_required
def friendsProfile():
    # try:
    #     conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
    #     print("Successful connection to the database!")
    # except:
    #     print("I am unable to connect to the database")

    # cur = conn.cursor()
    # user = current_user.first_name
    user = str(User.instances[0].first_name) + " " + str(User.instances[0].last_name)
    email = str(User.instances[0].email)
    username = str(User.instances[0].username)
    friendCount = _m.queryFriendCount(User.instances[0].id)
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
                           email=email,
                           username=username,
                           friendCount=friendCount,
                           posts=posts,
                           currentUser = False,
                           isFriend = False)

@app.route('/friendsList')
@login_required
def friendsList():
    friends = [
        {
            'username': 'Billy'
            },
        {
           'username': 'JohnBilly'
            }
    ]

    return render_template("friendsList.html",
                           friends = friends)

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
    # print (list10)
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


@app.route('/movieUpdate',methods=['POST','GET'])
def movieUpdate():
    global key

    imdbid = request.form['really']
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

@app.route('/rateMovie',methods=['POST','GET'])
def rateMovie():
    print("HI")
    rating = request.form['score']
    print (rating)
    return json.dumps({'status':'OK','score':rating})

@app.route('/BasicSearchResults',methods=['POST'])
def BasicSearchResults():
    global key
    titles = []
    year = []
    img = []
    ids = []
    searchterm = request.form['id']
    # print(imdbid)
    # title = imdb.get_title_by_id(imdbid)
    # print (title)
    sterms = imdb.search_for_title(searchterm)
    # print (sterms)



    for m in range (0,10):
        #image stuff
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
        # print (KEY)
        # print(m)
        r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=sterms[m]["imdb_id"]))
        api_response = r.json()

        keys = api_response.keys()
        # print (keys)
        # We have to handle errors for posters that we don't have
        if 'status_code' in api_response.keys():
            url = 'https://valleytechnologies.net/wp-content/uploads/2015/07/error.png'
            img.append(url)
        elif not api_response['posters']:
            url = 'https://valleytechnologies.net/wp-content/uploads/2015/07/error.png'
            img.append(url)
        else:
            rel_path = api_response['posters'][0]['file_path']
            url = "{0}{1}{2}".format(base_url, max_size, rel_path)
            img.append(url)
            ids.append(sterms[m]["imdb_id"])
        # img.append(imgtitle.trailer_image_urls[0])
        # img.append(imgtitle.image["url"])
        # print (imdb.get_title_images(sterm[m]["imdb_id"]))
        titles.append(sterms[m]["title"])
        year.append(sterms[m]["year"])
    return render_template("BasicSearchResults.html", img=img, title=titles, year=year,ids=ids)  # render the search results template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        #     error = 'Invalid Credentials. Please try again.'
        try:
            conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
            print("Successful connection to the database!")
        except:
            print("I am unable to connect to the database")
        cur = conn.cursor()
        try:
            cur.execute('\
                SELECT\
                    user_id,\
                    first_name,\
                    last_name,\
                    email,\
                    pass,\
                    username\
                FROM team3.user\
                WHERE\
                    (email = %s OR username = %s)\
                    AND pass = %s\
                ', (str(request.form['username']), str(request.form['username']), str(request.form['password'])))
        except psycopg2 as e:
            pass

        query_result = cur.fetchall()
        if (len(query_result) <= 0):
            error = 'Invalid Credentials. Please try again.'
        else:
            # login_user(User('user\'s id','firstname','lastname','email','password', 'username'))
            login_user(User(query_result[0][0],query_result[0][1],query_result[0][2],query_result[0][3],query_result[0][4],query_result[0][5]))
            return redirect(url_for('profile'))
    return render_template('login.html', error=error)

@app.route('/create', methods=['GET', 'POST'])
def creation():
    error1 = None
    error2 = None
    error3 = None
    if (request.method == 'POST'):
        try:
            conn = psycopg2.connect("dbname='kdjbimsf' user='kdjbimsf' host='pellefant-01.db.elephantsql.com' password='UwW8KkPi2TdrSmlxWMw54ARzmDFSXIFL'")
            print("Successful connection to the database!")
        except:
            print("I am unable to connect to the database")
        cur = conn.cursor()

        #Check to see if the user entered already exists
        valid_user = False
        valid_email = False

        cur.execute('SELECT * FROM team3.user WHERE username = %s', (request.form['username'],))
        if (len(cur.fetchall()) <= 0):
            valid_user = True

        cur = conn.cursor()

        cur.execute('SELECT * FROM team3.user WHERE email = %s', (request.form['email'],))
        if (len(cur.fetchall()) <= 0):
            valid_email = True

        if (not valid_user or not valid_email):
            error1 = "The following are/is invalid:"

        if (not valid_user):
            error2 = "Username is already taken"
        else:
            error2 = ""

        if (not valid_email):
            error3 = "Email is already taken"
        else:
            error3 = ""

        #   Both the user and the email are valid!
        if (valid_user and valid_email):

            #Insert into user
            cur = conn.cursor()
            try:
                cur.execute('\
                    INSERT INTO team3.user (first_name, last_name, email, pass, username) VALUES (\
                        %s,%s,%s,%s,%s)'
                        ,(
                        request.form['first_name'],
                        request.form['last_name'],
                        request.form['email'],
                        request.form['pass'],
                        request.form['username']
                        ))
                conn.commit()
            except psycopg2 as e:
                pass

            #Select the the user_id, which is needed to insert into friends, and posts
            cur = conn.cursor()
            try:
                cur.execute('\
                        SELECT\
                            user_id\
                        FROM team3.user\
                        WHERE\
                            username = %s\
                            OR email = %s\
                    ', (str(request.form['username']),str(request.form['email'])))
            except psycopg2 as e:
                pass

            results = cur.fetchall()
            referenceID = results[0][0]

            #Insert into friends
            cur = conn.cursor()
            try:
                cur.execute("\
                    INSERT INTO team3.friends (user_id, friend_id)\
                    VALUES (%s, '{}')\
                    ", (int(referenceID),))
                conn.commit()
            except psycopg2 as e:
                pass

            #Insert into posts
            #TODO

            #Now log that user in
            cur = conn.cursor()
            try:
                cur.execute('\
                    SELECT\
                        user_id,\
                        first_name,\
                        last_name,\
                        email,\
                        pass,\
                        username\
                    FROM team3.user\
                    WHERE\
                        (email = %s AND username = %s)\
                        AND pass = %s\
                    ', (str(request.form['email']), str(request.form['username']), str(request.form['pass'])))
            except psycopg2 as e:
                pass

            query_result = cur.fetchall()
            # if (len(query_result) <= 0):
            #     error = 'Invalid Credentials. Please try again.'
            # else:
            #     # login_user(User('user\'s id','firstname','lastname','email','password', 'username'))
            login_user(User(query_result[0][0],query_result[0][1],query_result[0][2],query_result[0][3],query_result[0][4],query_result[0][5]))
            return redirect(url_for('profile'))



    return render_template('profCreation.html', error1=error1, error2=error2, error3=error3)

#user_id is the unicode value of the user's id
@login_manager.user_loader
def load_user(user_id):
    #create instance of user of that id
    for x in range(0, len(User.instances)):
        if (str(User.instances[x].id) == str(user_id)):
            load_u = User.instances[x]


    # load_user = User.instances[0]
    if ('load_u' in locals()):
        return load_u

@app.route("/logout")
@login_required
def logout():
    User.instances = []
    logout_user()
    return redirect('/')
