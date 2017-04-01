from flask import Flask
import os

app = Flask(__name__)


#app.secret_key = os.environ['MY_SECRET_KEY']
app.secret_key = "ZoltaR2"

from app import views

from app import simple

from app import database
