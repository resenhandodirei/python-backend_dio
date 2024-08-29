from flask import Flask, Blueprint, request
from src.app import User, db
from http import HTTPStatus
from sqlalchemy import inspect
from flask_jwt_extended import jwt_required, get_jwt_identity, JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNDkzNzg3MywianRpIjoiOTljZDQzYzctNGExZi00ZDQ5LWExNDItOTE2OWRmZTYwMjI2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE3MjQ5Mzc4NzMsImNzcmYiOiI3NjIyMGNhNS0wMjJkLTQ4NzktYmVlNS04ZjZmYmZmMDczZmYiLCJleHAiOjE3MjQ5Mzg3NzN9.z85Sp_1ChjsWpXKjvy7bJThwnGfENgchn2YCB2u4jy8'  # Substitua pelo seu JWT secret
jwt = JWTManager(app)

app = Blueprint('user', __name__, url_prefix='/users')

def _create_user():
    data = request.json
    user = User(username=data['username'])
    db.session.add(user)
    db.session.commit()

def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id, 
            "username": user.username
        }
        for user in users
    ]

@app.route('/', methods=['GET', 'POST'])
@jwt_required()
def list_or_create_user():
    if request.method == 'POST':
        _create_user()
        return {"message": "User created"}, HTTPStatus.CREATED
    else: 
        return {"identity": get_jwt_identity(), "users": _list_users()}

@app.route('/<int:user_id>', methods=['GET'])
def get_user(user_id): 
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id,
        "username": user.username
    }

@app.route('/<int:user_id>', methods=['PATCH'])
def update_user(user_id): 
    user = db.get_or_404(User, user_id)
    data = request.json

    mapper = inspect(User)  # Ou JobStatus, se isso for necessário.
    for column in mapper.attrs:
        if column.key in data: 
            setattr(user, column.key, data[column.key])
    db.session.commit()
    
    return {
        "id": user.id,
        "username": user.username
    }

@app.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id): 
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()

    return "", HTTPStatus.NO_CONTENT
