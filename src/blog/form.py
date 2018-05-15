from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, SubmitField, TextField, TextAreaField
from wtforms import validators
from werkzeug.security import check_password_hash
from .models import User
from flask import flash


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[validators.DataRequired()])
    passwd = PasswordField("passwd", validators=[validators.DataRequired()])
    submit = SubmitField("提交")
    # recaptcha = RecaptchaField()

    def checkout_passwd(self):
        # print(self.data)
        email = self.data.get("email")
        passwd = self.data.get("passwd")
        try:
            user = User.query.filter_by(email=email).first()
            if check_password_hash(user.passwd, passwd):
                print("mima")
                return True
            else:
                return False
        
        except Exception as e:
            flash("用户不存在")


class TextInput(FlaskForm):
    
    title = TextField("title", validators=[validators.DataRequired()])
    absc = TextField("absc", validators=[validators.DataRequired()])
    context = TextAreaField("context", validators=[validators.DataRequired()])
    submit = SubmitField("提交")


class Resigner(FlaskForm):

    email = EmailField("emial", [
        validators.DataRequired("请填写邮件地址"), validators.Email()
        ])
    passwd = PasswordField("passwd", [
        validators.DataRequired("请输入密码"), validators.Length(6, 25)
        ])
    confirm = PasswordField("confirm", [
        validators.DataRequired("请再输入密码"), validators.EqualTo("passwd")
        ])
    submit = SubmitField("提交")
