from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["eventlogs"]

login_events = db["login_events"]