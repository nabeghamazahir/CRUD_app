from flask import Blueprint
from controllers.blog_controllers import index

blog_routes = Blueprint('blog_routes', __name__ )


blog_routes.route('')(index)