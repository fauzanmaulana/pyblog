from flask import Flask
import pymongo
from bson.json_util import dumps
import json
from settings import db, conn

client = pymongo.MongoClient(conn)

dbconn = pymongo.database.Database(client, db)

col = pymongo.collection.Collection(dbconn, 'users')

app = Flask(__name__)

@app.route("/")
def index():
    col.insert_one({'name':'bismillah'})
    return '<h1>added users was successfull!</h1>'

if(__name__ == "__main__"):
    app.run()