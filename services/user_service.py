from flask import request, jsonify
from models import session
from models.user import User

def create_user():
    data = request.get_json()
    user_admin = session.query(User).filter_by(email=data['email_admin']).first()
    if user_admin:
        if user_admin.is_admin == 1:
            # verificar se o email já esta cadastrado para outro usuario
            emailExists = session.query(User).filter_by(email=data['email']).first()
            if emailExists:
                return jsonify({'message': 'Email already exists'}), 409            
            
            new_user = User(nome=data['nome'], email=data['email'], telefone=data['telefone'], senha=data['senha'], is_admin=data['is_admin'])
            session.add(new_user)
            session.commit()
            return jsonify({'message': 'User created successfully by Admin'}), 201
        else:
            return jsonify({'message': 'User not authorized'}), 403
    else:
        return jsonify({'message': 'Bad request'}), 400    

def get_users():
    users = session.query(User).all()
    result = []
    for user in users:
        user_data = {
            'id': user.id,
            'nome': user.nome,
            'email': user.email,
            'telefone': user.telefone,
        }
        result.append(user_data)
    return jsonify(result)

def get_admins():
    users = session.query(User).filter_by(is_admin=1).all()
    result = []
    for user in users:
        user_data = {
            'id': user.id,
            'nome': user.nome,
            'email': user.email,
            'telefone': user.telefone,
            'senha': user.senha,
            'is_admin': user.is_admin
        }
        result.append(user_data)
    return jsonify(result)

def get_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user_data = {
            'id': user.id,
            'nome': user.nome,
            'email': user.email,
            'telefone': user.telefone,
        }
        return jsonify(user_data)
    else:
        return jsonify({'message': 'User not found'}), 404

def update_user(user_id):
    data = request.get_json()
    user_admin = session.query(User).filter_by(email=data['email_admin']).first()
    user = session.query(User).filter_by(id=user_id).first()    
    
    if user_admin:
        if user_admin.is_admin == 1:
            user.nome = data['nome']
            # verificar se o email já esta cadastrado para outro usuario
            emailExists = session.query(User).filter_by(email=data['email']).first()
            if emailExists and emailExists.id != user.id:
                return jsonify({'message': 'Email already exists'}), 409
            else:
                user.email = data['email']
            # user.email = data['email']
            user.telefone = data['telefone']
            user.senha = data['senha']
            user.is_admin = data['is_admin']
            session.commit()
            return jsonify({'message': 'User updated successfully by Admin'})
    else:
        if user:
            if data['email'] == user.email:
                user.nome = data['nome']
                user.telefone = data['telefone']
                user.senha = data['senha']
                session.commit()
                return jsonify({'message': 'User updated successfully'})
            else:
                return jsonify({'message': 'User not authorized'}), 403    
        else:
            return jsonify({'message': 'User not found'}), 404

def delete_user(user_id):
    data = request.get_json()
    user_admin = session.query(User).filter_by(email=data['email_admin']).first()

    if user_admin:
        if user_admin.is_admin == 1:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return jsonify({'message': 'User deleted successfully by Admin'})
            else:
                return jsonify({'message': 'User not found'}), 404
        else:
            return jsonify({'message': 'User not authorized'}), 403
    else:
        return jsonify({'message': 'Bad request'}), 400
