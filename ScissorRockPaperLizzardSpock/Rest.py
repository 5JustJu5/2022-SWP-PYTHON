import sqlite3
from flask import *
from flask_restful import Api
import ScissorRockPaperSpock

app = Flask(__name__)
api = Api(app)



            
@app.route('/')
def index():
    return ScissorRockPaperSpock.insertIntoDicto(True)

if __name__ == '__main__':
    app.run(port=8888,debug=True)