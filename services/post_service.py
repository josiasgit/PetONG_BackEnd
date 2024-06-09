from flask import request, jsonify
from models import session
from models.user import User
from models.post import Post

def create_post():
    data = request.get_json()
    # verificar se o usuário existe
    userExists = session.query(User).filter_by(id=data['user_id']).first()
    if userExists:
        new_post = Post(titulo=data['titulo'], conteudo=data['conteudo'], imagem_url=data['imagem_url'], user_id=data['user_id'])
        session.add(new_post)
        session.commit()
        return jsonify({'message': 'Post created successfully'}), 201
    else:
        return jsonify({'message': 'User not found'}), 404
    
def get_posts():
    posts = session.query(Post).all()
    result = []
    for post in posts:
        post_data = {
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'imagem_url': post.imagem_url,
            'user_id': post.user_id
        }
        result.append(post_data)
    return jsonify(result)

def get_post(post_id):
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        post_data = {
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'imagem_url': post.imagem_url,
            'user_id': post.user_id
        }
        return jsonify(post_data)
    else:
        return jsonify({'message': 'Post not found'}), 404

def get_post_byUser(user_id):
    posts = session.query(Post).filter_by(user_id=user_id).all()
    result = []
    for post in posts:
        post_data = {
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'imagem_url': post.imagem_url,
            'user_id': post.user_id
        }
        result.append(post_data)
    return jsonify(result)

def update_post(post_id):
    data = request.get_json()
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        if data['user_id'] != post.user_id:
            return jsonify({'message': 'User not authorized'}), 403

        post.titulo = data['titulo']
        post.conteudo = data['conteudo']
        post.imagem_url = data['imagem_url']
        session.commit()
        return jsonify({'message': 'Post updated successfully'}), 200
    else:
        return jsonify({'message': 'Post not found'}), 404

def delete_post(post_id):
    data = request.get_json()
    user_admin = session.query(User).filter_by(email=data['email_admin']).first()
    post = session.query(Post).filter_by(id=post_id).first()
    
    if post:
        if user_admin:
            if user_admin.is_admin == 1 or data['user_id'] == post.user_id:
                session.delete(post)
                session.commit()
                return jsonify({'message': 'Post deleted successfully'}), 200
            else:
                return jsonify({'message': 'User not authorized'}), 403
        else:
            return jsonify({'message': 'User not found'}), 404