# 데이터를 Mongo.DB에 올리기

from pymongo import MongoClient
import json

HOST = 'cluster0.ko4ju.mongodb.net'
USER = 'JYPuser'
PASSWORD = 'JYPuserpassword'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'board_games'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

import pandas as pd

data = pd.read_csv('project3.csv')

json_data = data.to_json(orient = 'records')

dic_data = json.loads(json_data)

collection.insert_many(dic_data)