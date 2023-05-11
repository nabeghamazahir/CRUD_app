import os
from flask import Flask, redirect
from dotenv import load_dotenv


from routes.blog_routes import blog_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

load_dotenv()

SECRET_KEY = os.getenv('API_KEYS')


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(blog_routes, url_prefix='/blog')
app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')


@app.route('/')
def index():
    return redirect('/blog')