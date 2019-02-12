# flask_web/app.py

from flask import Flask
from flask import jsonify

app = Flask(__name__)

userdata = [
    {
        'name':'eli',
        'email':'elisabeth.leonhardt@dinocloudconsulting.com'
    },
    {
        'name':'juan',
        'email':'juancito@gmail.com'

    },
    {
        'name':'pepe',
        'email':'pepe123@gmail.com'
    }
        

]

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hey, from the Flask Docker container!'
    
@app.route('/users', methods=['GET'])
def see_users():
    return jsonify(userdata)

@app.route('/hello2')
def other_function():
    return 'hello from my python3.6 dockerized flask app'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
