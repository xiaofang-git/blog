# 判断登录模块
from functools import wraps
from flask import session, redirect, url_for, make_response, request


def judge_login(func):
    # 判断是否登录
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "login" in session and session["login"]:
            return func(*args, **kwargs)
        else:
            response = make_response(redirect(url_for("admin.login")))
            response.set_cookie("original_url", request.url)
            return response
        
    return wrapper
