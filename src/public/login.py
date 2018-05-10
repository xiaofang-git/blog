# 判断登录模块
from functools import wraps
from flask import session, redirect, url_for


def judge_login(func):
    # 判断是否登录
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session["login"]:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("admin.login"))
        
    return wrapper
