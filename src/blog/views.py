from flask import Blueprint, url_for, render_template, redirect, session
from .form import LoginForm, TextInput
from .models import Blog, db
from public.login import judge_login
import datetime


blog = Blueprint('blog', __name__, template_folder="templates", static_folder="static")


@blog.route("/")
def index():
    context = Blog.query.all()
    return render_template("index.html", context=context)


@blog.route("/<int:blog_id>")
def comment(blog_id):
    context = Blog.query.filter_by(id=blog_id).first()
    return render_template("comment.html", context=context)


@blog.route("/new", methods=["GET", "POST"])
@judge_login
def new():
    form = TextInput()
    if form.validate_on_submit():
        title = form.data.get("title")
        absc = form.data.get("absc")
        context = form.data.get("context")
        tag = "默认"
        blog = Blog(title=title, absc=absc, context=context, tag=tag, ptime="2017-02-18", user_id=4)
        db.session.add(blog)
        db.session.commit()
        return "seccess"

    return render_template("new.html", context={}, form=form)


