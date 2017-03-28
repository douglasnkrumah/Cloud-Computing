from flask import Flask
import os

app = Flask(__name__)

app.secret_key = os.environ['MY_SECRET_KEY']

from app import views, simple, database
