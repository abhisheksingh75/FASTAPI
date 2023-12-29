from pymongo import MongoClient
client = MongoClient("<mongodb_connection_url>")

db = client.books_database
collection_name = db["books_collection"]