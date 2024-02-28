from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """This brings a user to the home page of the app"""
    return 'The main page'