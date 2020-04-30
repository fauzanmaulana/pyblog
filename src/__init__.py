from flask import Flask, render_template
from bson.json_util import dumps
import json
from .connections import client, dbconn, pymongo

col = pymongo.collection.Collection(dbconn, 'users')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

if(__name__ == "__main__"):
    app.run()