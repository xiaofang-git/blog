from flask import Flask, url_for, render_template, redirect, request, abort
from .models import Session, Blog
import time


app = Flask(__name__)


@app.route("/")
def index():
    session = Session()
    context = {
        'login': url_for("login"),
        'logout': url_for("logout"),
        "comment": url_for("comment", tid=""),
        "new": url_for("new"),
        'blogs': session.query(Blog)
    }
    session.close()
    return render_template("index.html", context=context)


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        context = {}
        return render_template("new.html", context=context)
    elif request.method == "POST":
        title = request.form["title"]
        context = request.form["text"]
        ptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        absc = request.form["absc"]
        session = Session()
        result = Blog(title=title, absc=absc, ptime=ptime, context=context)
        session.add(result)
        session.commit()
        session.close()
        return "提交成功"


@app.route("/login", methods=['GET', "POST"])
def login():
    context = {
        "register": url_for("register"),
    }
    if request.method == "GET":
        return render_template("login.html", context=context)
    if request.method == "POST":
        return "登陆成功"


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


@app.route("/comment/<tid>")
def comment(tid):
    # abort(401)
    return tid


@app.route("/register")
def register():
    return "欢迎注册"