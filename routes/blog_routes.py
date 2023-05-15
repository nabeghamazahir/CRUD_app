from flask import Blueprint
from controllers.blog_controllers import index, create, edit , update_post, delete_post, category_blog

blog_routes = Blueprint('blog_routes', __name__ )


blog_routes.route('')(index)
blog_routes.route('/post', methods=['POST'])(create)
blog_routes.route('/<id>/edit')(edit)
blog_routes.route('/update/<id>', methods=["POST"])(update_post)
blog_routes.route('/<id>/delete', methods=["POST"])(delete_post)
blog_routes.route('/category')(category_blog)
