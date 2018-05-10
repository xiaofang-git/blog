from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from .models import User
from flask import flash


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    passwd = PasswordField("passwd", validators=[DataRequired()])
    submit = SubmitField("提交")
    # recaptcha = RecaptchaField()

    def checkout_passwd(self):
        # print(self.data)
        email = self.data.get("email")
        passwd = self.data.get("passwd")
        try:
            user = User.query.filter_by(email=email).first()

            if check_password_hash(user.passwd, passwd):
                return True
            else:
                return False
        
        except Exception as e:
            flash("用户不存在")


class TextInput(FlaskForm):
    
    title = TextField("title", validators=[DataRequired()])
    absc = TextField("absc", validators=[DataRequired()])
    context = TextAreaField("context", validators=[DataRequired()])
    submit = SubmitField("提交")
