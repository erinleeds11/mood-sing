from flask import Flask, render_template, request, flash, session, redirect, jsonify
import os
import requests
from jinja2 import StrictUndefined
import json
from random import choice, randint

# API_KEY = os.environ['SPOTIFY_KEY']
app = Flask(__name__)
app.secret_key = "abc"
app.jinja_env.undefined = StrictUndefined

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template('root.html')

@app.route('/')
def homepage():
    """Homepage"""

    return render_template("root.html")


if __name__ == '__main__':
    # connect_to_db(app, echo=False)
    app.run(host='0.0.0.0')

