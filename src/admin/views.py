from . import admin
from flask import render_template, request, redirect, url_for, session
from blog.models import Blog, User, db
from flask_sqlalchemy import SQLAlchemy
from blog.form import LoginForm, Resigner
from public.login import judge_login
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


@admin.route("/drop")
@judge_login
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

    if "login" in session and session["login"]:
        return render_template("admin.html", context=Blog.query.all())
    else:
        login_form = LoginForm()
        if login_form.validate_on_submit():
            if login_form.checkout_passwd():
                session["login"] = True
                session["user"] = login_form.data.get("email")
                original_url = request.cookies.get("original_url")
                if original_url:
                    return redirect(original_url)
                else:
                    return render_template("admin.html", context=Blog.query.all())

        return render_template("login.html", context={}, form=login_form)


@admin.route("/logout")
def logout():
    session["login"] = False
    return redirect(url_for("admin.login"))


@admin.route("/register", methods=["GET", "POST"])
def register():
    form = Resigner()
    if form.validate_on_submit():
        email = form.data.get("email")
        passwd = generate_password_hash(form.data.get("passwd"))
        print(email, passwd)
        user = User(email=email, passwd=passwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("admin.login"))
    return render_template("register.html", form=form)