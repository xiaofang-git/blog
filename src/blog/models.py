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
    tag = db.Column(db.String(45))
    ptime = db.Column(db.String(50))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))    


class User(db.Model):
    __bind_key__ = 'users'
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(45))
    passwd = db.Column(db.String(100))
    nick = db.Column(db.String(45))
    age = db.Column(db.String(45))
    gender = db.Column(db.String(45))
    createtime = db.Column(db.String(45))
    blogs = db.relationship("Blog", backref="user")   
