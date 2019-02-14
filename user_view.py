from flask_classy import FlaskView
from flask import jsonify, request
from datetime import datetime
from werkzeug.exceptions import BadRequest, InternalServerError
import schemas
from models import User
from database import db
from utils import authorization


class UserView(FlaskView):
    user_schema = schemas.UserSchema()
    
    def index(self):
        users = User.query.all()
        users_data = self.user_schema.dump(users, many=True).data
        return jsonify(users_data)

    def post(self):
        userdata = request.json
        access_data = request.authorization
        print(access_data)
        username = userdata.get('username', None)
        password = userdata.get('password', None)
        name = userdata.get('name', None)
        lastname = userdata.get('lastname', None)
        birthday = userdata.get('birthday', None)

        if not username:
            raise BadRequest('Username name is None')

        if not password:
            raise BadRequest('Password name is None')

        if not name:
            raise BadRequest('Name name is None')
        
        if not lastname:
            raise BadRequest('Last name is None')
        
        if not birthday:
            raise BadRequest('Birthday is None')

        #convert birthday into date
        format_str = '%d/%m/%Y' # The format
        datetime_obj = datetime.strptime(birthday, format_str)
        
        user = User(username=username, password=password, name=name, lastname=lastname, birthday=datetime_obj)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            import pdb; pdb.set_trace()
            print(e)
            db.session.rollback()
            raise InternalServerError('User not added')
        user_data = self.user_schema.dump(user).data
        return jsonify({'user': user_data})

    def get(self, id_user):
        user = User.query.filter_by(id_user = id_user).first()
        print(user)
        user_data = self.user_schema.dump(user).data
        return jsonify(user_data)

    def put(self, id_user):
        userdata = request.json
        username = userdata.get('username', None)
        password = userdata.get('password', None)
        name = userdata.get('name', None)
        lastname = userdata.get('lastname', None)
        birthday = userdata.get('birthday', None)
        user = User.query.filter_by(id_user=id_user).first()
        try:
            if username:
                user.username = username
            if password:
                user.password = password
            if name:
                user.name = name
            if lastname:
                user.lastname = lastname
            if birthday:
                format_str = '%d/%m/%Y' # The format
                datetime_obj = datetime.strptime(birthday, format_str)
                user.birthday = datetime_obj


            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise InternalServerError('User not modified')
        
        user = User.query.filter_by(id_user = id_user).first()
        user_data = self.user_schema.dump(user).data

        return jsonify(user_data)


    def delete(self, id_user):
        if authorization():
            try:
                User.query.filter_by(id_user = id_user).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise InternalServerError('User not deleted')
            return 'User deleted succesfully'
        else:
            return 'authorization failed!'