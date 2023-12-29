from pymongo import MongoClient
client = MongoClient("mongodb")

db = client.books_database
collection_name = db["books_collection"]