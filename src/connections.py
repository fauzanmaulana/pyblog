import pymongo
from .settings import db, conn

client = pymongo.MongoClient(conn)

dbconn = pymongo.database.Database(client, db)