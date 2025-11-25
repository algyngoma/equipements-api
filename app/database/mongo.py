from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
db = client["equipements_db"]
equipements_collection = db["equipements"]
