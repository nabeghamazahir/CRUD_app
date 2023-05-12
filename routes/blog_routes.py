from flask import Blueprint
from controllers.blog_controllers import index, create

blog_routes = Blueprint('blog_routes', __name__ )


blog_routes.route('')(index)
blog_routes.route('/post', methods=['POST'])(create)