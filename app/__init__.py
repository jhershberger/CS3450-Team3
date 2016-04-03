from flask import Flask
import os
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager()
login_manager.init_app(app)

from app import views

print("app: ", app)
