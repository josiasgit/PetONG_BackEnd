from flask import Blueprint
from services import user_service

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['POST'])(user_service.create_user)
user_bp.route('/users', methods=['GET'])(user_service.get_users)
user_bp.route('/admins', methods=['GET'])(user_service.get_admins)
user_bp.route('/users/<int:user_id>', methods=['GET'])(user_service.get_user)
user_bp.route('/users/<int:user_id>', methods=['PUT'])(user_service.update_user)
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(user_service.delete_user)
