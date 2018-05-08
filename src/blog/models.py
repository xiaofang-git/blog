from flask_sqlalchemy import SQLAlchemy
# from src.main import app

# from flask import Flask
# app = Flask("blog")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0805@127.0.0.1:3306/blog'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy()


class Blog(db.Model):

    __tablename__ = "blog"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))
    absc = db.Column(db.String(50))
    context = db.Column(db.Text())
    ptime = db.Column(db.String(50))


class User(db.Model):
    __bind_key__ = 'users'
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(50))
    passwd = db.Column(db.String(100))

