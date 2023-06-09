from flask import render_template, request, redirect, session
from models.users import find_user_by_email
from models.blogs import myblog, find_post_owner
from services.session_info import current_user
import bcrypt

def new():
  return render_template('/sessions/new.html')

def post():
  return render_template('/sessions/post.html')

def create():
  email = request.form.get('email')
  password = request.form.get('password')
  user = find_user_by_email(email)
  if user == None:
    return redirect('/sessions/new')

  valid_password = bcrypt.checkpw(password.encode(), user['password_digest'].encode())
  if valid_password:
    session['user_id'] = user['id'] # logs the user in
    return redirect('/')
  else:
    return redirect('/sessions/new')
  
def delete():
  session.clear() # logs the user out
  return redirect('/')

def single_post(id):
  post = myblog(id)
  post_owner = find_post_owner(id)[0]['user_id']
  return render_template('/sessions/myblog.html', posts = post, current_user = current_user, post_owner = post_owner )
