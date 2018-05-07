from flask import Blueprint, url_for, render_template, redirect
from .form import LoginForm, TextInput
from .models import Blog, db

blog = Blueprint('blog', __name__, template_folder="templates", static_folder="static")


@blog.route("/")
def index():
    return render_template("index.html", context={})


@blog.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.checkout_passwd():
            return "success"
    return render_template("login.html", context={}, form=login_form)


@blog.route("/new", methods=["GET", "POST"])
def new():
    form = TextInput()
    if form.validate_on_submit():
        title = form.data.get("title")
        absc = form.data.get("absc")
        context = form.data.get("context")
        blog = Blog(title=title, absc=absc, context=context)
        db.session.add(blog)
        db.session.commit()
        return "seccess"

    return render_template("new.html", context={}, form=form)


@blog.route("/logout")
def logout():
    return redirect(url_for("blog.login"))