import pickle

model = None

with open('model.pkl','rb') as pickle_file:
    model = pickle.load(pickle_file)

X_test = [{'Min Players':1, 'Max Players':3, 'Play Time':90, 'Complexity Average':2, 'Domain1':'Thematic Games', 'Domain2':''}]

print(model.predict(X_test)[0])