from flask import Blueprint, url_for, render_template, redirect
from .form import LoginForm

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


@blog.route("/new")
def new():
    return render_template("new.html", context={})


@blog.route("/logout")
def logout():
    return redirect(url_for("blog.login"))