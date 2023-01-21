import sqlite3
from flask import *
from flask import Flask, render_template
from flask_restful import Api
import ScissorRockPaperSpock

app = Flask(__name__)
api = Api(app)


            
@app.route('/')
def index():
    #return ScissorRockPaperSpock.insertIntoDicto(True)
    return render_template('startseite.html')

@app.route('/stats')
def statss():
    daten = ScissorRockPaperSpock.insertIntoDicto(True)
    daten2 = []
    for i in daten:
        if i[4] == 1:
           daten2.append(i)
    
    spieler = 0
    com = 0
    unen = 0
    for i in daten2:
        if i[3] == 1:
            spieler += 1
        if i[3] == 2:
            com += 1
        if i[3] == 3:
            unen += 1
    
    return render_template("stats.html", daten = daten2, spieler = spieler*15, com = com*15, unen = unen*15)

    
@app.route('/game')
def spielen():
    pass
    

        
if __name__ == '__main__':
    app.run(port=8888,debug=True)
    