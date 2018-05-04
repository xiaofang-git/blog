from flask import Flask, url_for, render_template, redirect, request


app = Flask(__name__)


@app.route("/")
def index():
    context = {
        'login': url_for("login"),
        'logout': url_for("logout"),
        "comment": url_for("comment", tid=""),
        'blogs': [
            {
                'title': "为自由",
                "tid": 1,
                "desc": "活着不就是为了自由么"
                },
            {
                "title": "为生活",
                "tid": 2,
                "desc": "活着不就是为了自由么"},
            {
                "title": "为梦想",
                "tid": 3,
                "desc": "活着不就是为了自由么"}
            ],
    }
    return render_template("index.html", context=context)


@app.route("/login", methods=['GET', "POST"])
def login():
    context = {}
    if request.method == "GET":
        return render_template("login.html", context=context)
    if request.method == "POST":
        return "登陆成功"


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


@app.route("/comment/<tid>")
def comment(tid):
    return tid