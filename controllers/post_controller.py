from flask import Blueprint
from services import post_service

post_bp = Blueprint('post_bp', __name__)

post_bp.route('/posts', methods=['POST'])(post_service.create_post)
post_bp.route('/posts', methods=['GET'])(post_service.get_posts)
post_bp.route('/posts/<int:post_id>', methods=['GET'])(post_service.get_post)
post_bp.route('/posts/user/<int:user_id>', methods=['GET'])(post_service.get_post_byUser)
post_bp.route('/posts/<int:post_id>', methods=['PUT'])(post_service.update_post)
post_bp.route('/posts/<int:post_id>', methods=['DELETE'])(post_service.delete_post)
