CREATE DATABASE post_mate;

/c post_mate

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT UNIQUE,
  password_digest TEXT NOT NULL 
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  category TEXT,
  user_id INTEGER NOT NULL
);

ALTER TABLE posts
ADD COLUMN users_id TEXT;
