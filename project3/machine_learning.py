from pymongo import MongoClient
import json
import pandas as pd
from category_encoders import OrdinalEncoder, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
import load_database as ld

data = ld.data

# 머신러닝
target = 'Name'
features = data.drop(columns=[target]).columns

X_train = data[features]
y_train = data[target]

model = make_pipeline(
    OneHotEncoder(), 
    DecisionTreeClassifier()
)

model.fit(X_train, y_train)

# 피클링

import pickle

with open('model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)

# 실행 테스트
# print(model.predict([{'Min Players':2, 'Max Players':2, 'Play Time':60, 'Complexity Average':2.06, 'Domain1':'Thematic Games', 'Domain2':''}]))