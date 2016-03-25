from flask import render_template
from app import app

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
