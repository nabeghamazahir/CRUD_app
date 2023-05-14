from db.db import sql

def all_posts():
  return sql('SELECT * FROM posts')

def create_post(title, body, category):
  sql('INSERT INTO posts(title, body, category) VALUES(%s, %s, %s) RETURNING *', [title, body, category])