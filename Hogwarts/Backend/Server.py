
from SqlConnection import getSqlConnection
from flask import Flask,jsonify,request
import Students_dao

app = Flask(__name__)
Connection=getSqlConnection()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Students')
def getStudents():
    S=Students_dao.getAllStudents(Connection)
    response=jsonify(S)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    
    
if __name__=='__main__':
    app.run(debug=True)
