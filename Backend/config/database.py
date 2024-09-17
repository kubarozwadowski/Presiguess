from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongo_uri)

db = client.president_db

collection_name = db["president_collection"]