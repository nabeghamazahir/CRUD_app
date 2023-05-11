from flask import Blueprint
from controllers.users_controllers import new, create

users_routes = Blueprint('users_routes', __name__)

users_routes.route('/new')(new)
users_routes.route('', methods=["POST"])(create)