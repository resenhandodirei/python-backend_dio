from flask import Blueprint, request
from src.app import Role, db
from http import HTTPStatus
from flask_jwt_extended import jwt_required

role_bp = Blueprint('roles', __name__, url_prefix='/roles')

@role_bp.route('/', methods=['POST'])
@jwt_required()  # Exige que o usuário esteja autenticado
def create_role():
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()
    
    return {'msg': 'Role created successfully'}, HTTPStatus.CREATED
