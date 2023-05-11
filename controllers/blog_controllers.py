from flask import render_template, request, redirect
from db.db import sql
# from models.blogs  
from services.session_info import current_user

def index():
  
  return render_template('blog/index.html', current_user=current_user)
