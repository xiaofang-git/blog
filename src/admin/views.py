from . import admin
from flask import render_template, request, redirect, url_for
from blog.models import Blog
from flask_sqlalchemy import SQLAlchemy
from blog.form import LoginForm

db = SQLAlchemy()


@admin.route("/drop")
def drop():
    blog_id = request.args.get("blog_id")
    try:
        blog_id = int(blog_id)
    except Exception as e:
        return "参数有误"

    blog = Blog.query.get_or_404(blog_id)
    if blog:
        blog = db.session.query(Blog).filter(Blog.id==blog_id).first()
        db.session.delete(blog)
        db.session.commit()
        return "删除成功"


@admin.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.checkout_passwd():
            return render_template("admin.html", context=Blog.query.all())

    return render_template("login.html", context={}, form=login_form)


@admin.route("/logout")
def logout():
    return redirect(url_for("admin.login"))