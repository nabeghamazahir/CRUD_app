from db.db import sql

def all_posts():
  return sql('SELECT * FROM posts')

def create_post(title, body, category, user_id):
  sql('INSERT INTO posts(title, body, category, user_id) VALUES(%s, %s, %s, %s) RETURNING *', [title, body, category, user_id])

def myblog(id):
  return sql('SELECT * FROM posts WHERE id =%s',[id])
def find_post_owner(id):
  return sql('SELECT user_id FROM posts where id=%s',[id])

def update(title, body, category, user_id, id):
  sql('UPDATE posts SET title=%s, body=%s, category = %s, user_id=%s WHERE id=%s RETURNING *', [title, body, category, user_id, id])


def category_posts(category):
  return sql('SELECT * FROM posts WHERE category=%s', [category])

def delete(id):
  sql('DELETE FROM posts WHERE id=%s RETURNING *', [id])