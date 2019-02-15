from flask_classy import FlaskView
from flask import jsonify, request
from datetime import datetime
from werkzeug.exceptions import BadRequest, InternalServerError
from schemas import *
from models import Task, TaskStatus, User
from database import db
from utils import authorization




class TasksView(FlaskView):
    task_schema = TaskSchema()
    status_schema = TaskStatusSchema()

    def index(self):
        user = authorization()
        tasks = Task.query.filter_by(id_user = user.id_user).all()
        tasks_data = self.task_schema.dump(tasks, many=True).data
        return jsonify(tasks_data)

    def get(self, id_task):
        user = authorization()
        if user is None:
            raise BadRequest('No user found')
        task = Task.query.filter(Task.id_task==int(id_task), Task.id_user==user.id_user ).first()
        task_data = self.task_schema.dump(task).data
        return jsonify({'task': task_data})

    def post(self):
        #add fields, queries, try/catch, etc
        user = authorization()
        print(user.id_user)
        if user is None:
            raise BadRequest('No user found')
        
        data = request.json
        task_name = data.get('task_name', None)
        task_description = data.get('description', None)
        if not task_name:
            raise BadRequest('Task name is None')
        
        #encontrar description id, add if it does not exist
        status = TaskStatus.query.filter_by(description = task_description).first()
        print(status)
        if status is None:
            status = TaskStatus(description = task_description)
            try:
                db.session.add(status)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise InternalServerError('TaskStatus not added')
        
        print(task_name, user.id_user, task_description)

        tsk = Task(task_name=task_name, id_user = user.id_user, id_task_status=status.id_task_status)
        try:
            db.session.add(tsk)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise InternalServerError('Task not added')
        task_data = self.task_schema.dump(tsk).data
        return jsonify({'task': task_data})

    def put(self, id_task):
        user = authorization()
        #sacar los datos del request
        data = request.json
        task_name = data.get('task_name', None)
        task_description = data.get('description', None)

        mytask = Task.query.filter_by(id_task = id_task).first()
        mystatus = TaskStatus.query.filter_by(description = task_description).first()

        if task_name:
            mytask.task_name = task_name
        if task_description:
            mytask.id_task_status = mystatus.id_task_status
        
        try:
            db.session.commit()
        except Exception as e:
            raise InternalServerError('Task could not be deleted')
        task_data = self.task_schema.dump(mytask).data
        return jsonify(task_data)


    def delete(self, id_task):
        user = authorization()
        task = Task.query.filter(Task.id_task==int(id_task), Task.id_user==user.id_user).first()
        try:
            db.session.delete(task)
            db.session.commit()
        except Exception as e:
            raise InternalServerError('Task could not be deleted')
        return 'Task deleted succesfully'
