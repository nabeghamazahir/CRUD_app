from flask import render_template, request, redirect
from db.db import sql
from models.blogs import all_posts, create_post
from services.session_info import current_user

def index():
  posts = all_posts()
  return render_template('blog/index.html', posts = posts, current_user=current_user)


def create():
  title = request.form.get('title')
  body = request.form.get('body')
  create_post(title, body)
  return redirect('/')