# flask_web/app.py

from flask import Flask
from flask import jsonify
from user_view import UserView
from task_view import TasksView

from database import create_app, db
from flask_cors import CORS

app = create_app()

#register views
UserView.register(app)
TasksView.register(app)

if __name__ == '__main__':
    with app.app_context():
        CORS(app)
        db.create_all() #knows if the database is already there?
        app.run(host='0.0.0.0', debug=True)