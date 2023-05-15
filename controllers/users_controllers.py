from flask import render_template, request, redirect
from db.db import sql
from models.users import create_user, find_user_by_email

def new():
  return render_template('users/new.html')



def create():
  first_name = request.form.get('first_name')
  last_name = request.form.get('last_name')
  email = request.form.get('email')
  password = request.form.get('password')
  user = find_user_by_email(email)
  if user == None:
    create_user(first_name, last_name, email, password)
    return redirect('/')
  else:
    message = "Email already exists"
    return render_template('users/new.html',message = message)
    
