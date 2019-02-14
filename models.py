from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, String, Date
import datetime
from datetime import date
from database import db


class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(Integer, primary_key=True)
    username = db.Column(String(150), nullable=False)
    password = db.Column(String(150), nullable=False)
    name = db.Column(String(150), nullable=False)
    lastname = db.Column(String(150), nullable=False)
    birthday = db.Column(Date)

    def __init__(self, username=None, password=None, name=None, lastname=None, birthday=None):
        self.username = username
        self.password = password
        self.name = name 
        self.lastname = lastname
        self.birthday = birthday
        
    class Task(db.Model):
        __tablename__ = 'tasks'
        id_task = db.Column(Integer, primary_key=True)
        task_name = db.Column(String(150), nullable=False)
        id_task_status = db.Column(Integer, ForeignKey('task_statuses.id_task_status'))
        description = db.relationship('TaskStatus', backref=db.backref('task status per task'))
        id_user = db.Column(Integer, ForeignKey('users.id_user'))

        def __init__(self, task_name=None, id_task_status=1):
            self.task_name = task_name
            self.id_task_status = id_task_status

    class TaskStatus(db.Model):
        __tablename__ = 'task_statuses'
        id_task_status = db.Column(Integer, primary_key=True)
        description = db.Column(String(70))

        def __init__(self, id_task_status=None, description=None):
            self.id_task_status = id_task_status
            self.description = description