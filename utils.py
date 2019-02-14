from werkzeug.exceptions import NotFound
from flask import request
import base64
import schemas
from models import User
from database import db

def authorization():
    auth = request.authorization
    username = auth.username
    password = auth.password

    user = User.query.filter_by(username = username).first()
    if (user.username == username and user.password == password):
        print("user succesfully authenticated")
        return user
    else:
        print("problem with user authentication")
        return None 
    
   