# 머신러닝 모델이 담긴 피클 가져오기

import pickle

model = None

with open('model.pkl','rb') as pickle_file:
    model = pickle.load(pickle_file)

# 머신러닝에 사용한 데이터 가져오기

import load_database as ld

data = ld.data
data_id = ld.data_id

# 플라스크 제작

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
 
@app.route('/',methods=['Get','POST'])
@app.route('/min<num1>/max<num2>/time<num3>/complexity<num4>/<game>')
def inputTest(num1=None, num2=None, num3=None, num4=None, game=None):
    if request.method == 'GET':
        return render_template('main.html',num1=num1, num2=num2, num3=num3, num4=num4, game=game)
    if request.method == 'POST':
        return render_template('main.html',num1=None, num2=None, num3=None, num4=None, game=None)

@app.route('/input',methods=['POST'])
def input(num1=None, num2=None, num3=None, num4=None, domain1=None, domain2=None):
    if request.method == 'POST':
        temp1 = request.form['num1']
        temp2 = request.form['num2']
        temp3 = request.form['num3']
        temp4 = request.form['num4']
        temp5 = request.form['domain1']
        temp6 = request.form['domain2']
    else:
        temp1 = None
        temp2 = None
        temp3 = None
        temp4 = None
        temp5 = None
        temp6 = None
    return redirect(url_for('answer',num1=temp1, num2=temp2, num3=temp3, num4=temp4, domain1=temp5, domain2=temp6))

@app.route('/<num1>/<num2>/<num3>/<num4>/<domain1>/<domain2>')
def answer(num1=None, num2=None, num3=None, num4=None, domain1=None, domain2=None):
    X_test = [{'Min Players':num1, 'Max Players':num2, 'Play Time':num3, 'Complexity Average':num4, 'Domain1':domain1, 'Domain2':domain2}]
    game = model.predict(X_test)[0]
    return redirect(url_for('game',game=game))

@app.route('/<game>')
def game(game):
    min_players = data[data['Name']==game]['Min Players'].iloc[0]
    max_players = data[data['Name']==game]['Max Players'].iloc[0]
    play_time = data[data['Name']==game]['Play Time'].iloc[0]
    complexity = data[data['Name']==game]['Complexity Average'].iloc[0]
    ID = data_id[data_id['Name']==game]['ID'].iloc[0]
    if data[data['Name']==game]['Domain1'].iloc[0]=='Unclassified':
        game_domain = ''
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Strategy Games":
        game_domain = '전략'
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Thematic Games":
        game_domain = '테마'
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Abstract Games":
        game_domain = '추상'
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Wargames":
        game_domain = '전쟁'
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Party Games":
        game_domain = '파티'
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Family Games":
        game_domain = '가족'
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Children's Games":
        game_domain = '어린이'
    elif data[data['Name']==game]['Domain1'].iloc[0]=="Customizable Games":
        game_domain = '커스텀'
    return render_template('main.html',game=game,min_players=min_players,max_players=max_players,play_time=play_time,complexity=complexity,game_domain=game_domain,ID=ID)
    
if __name__ == '__main__':
    app.run(debug=True)