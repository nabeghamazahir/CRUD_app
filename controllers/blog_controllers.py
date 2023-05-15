from flask import render_template, request, redirect
from models.blogs import myblog, all_posts, create_post, update, delete, category_posts
from services.session_info import current_user

def index():
  posts = all_posts()
  return render_template('blog/index.html', posts = posts, current_user=current_user)


def create():
  title = request.form.get('title')
  body = request.form.get('body')
  category = request.form.get('category')
  category = str(category)
  user_id = current_user()['id']

  create_post(title, body, category, user_id)
  return redirect('/')

def edit(id):
  post = myblog(id)[0]
  return render_template('sessions/update.html', post=post)

def update_post(id):
  title = request.form.get('title')
  body = request.form.get('body')
  category = request.form.get('category')
  category = str(category)
  user_id = current_user()['id']
  update(title, body, category, user_id, id)
  return redirect('/')

def delete_post(id):
  delete(id)
  return redirect('/')

def category_blog():
  category = request.args.get('c')
  posts = category_posts(category)
  return render_template('blog/categories.html', posts = posts, current_user=current_user)