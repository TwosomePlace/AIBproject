import pandas as pd
from pymongo import MongoClient

HOST = 'cluster0.ko4ju.mongodb.net'
USER = 'JYPuser'
PASSWORD = 'JYPuserpassword'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'board_games'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

data = pd.DataFrame(list(collection.find({"BGG Rank":{'$lte': 2000}}, {'_id' : 0 , 'ID' : 0,'Year Published' : 0,'Min Age': 0,'Users Rated' : 0, 'Rating Average' : 0, 'BGG Rank' : 0,'Owned Users' : 0,'Mechanics' : 0})))

data_id = pd.DataFrame(list(collection.find({"BGG Rank":{'$lte': 2000}}, {'_id' : 0 , 'Name' : 1, 'ID' : 1})))