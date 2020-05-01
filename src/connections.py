import pymongo
from .settings import db, conn, secret_keys

client = pymongo.MongoClient(conn)

dbconn = pymongo.database.Database(client, db)

usercoll = pymongo.collection.Collection(dbconn, 'users')
blogcoll = pymongo.collection.Collection(dbconn, 'blogs')
