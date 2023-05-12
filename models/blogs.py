from db.db import sql

def all_posts():
  return sql('SELECT * FROM posts')
def create_post(title, body):
  sql('INSERT INTO posts(title, body) VALUES(%s, %s) RETURNING *', [title, body])