import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://DmitrijsVaseckins:flask@cluster0.kdube.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["users"]
collection = db["users"]

post = {"_id": 2, "name": "Dmitrijs", "last name": "Vaseckins"}

collection.insert_one(post)