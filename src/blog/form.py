from flask_wtf import Form, RecaptchaField
from flask_wtf.html5 import EmailField
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from .models import User


class LoginForm(Form):
    email = EmailField('email', validators=[DataRequired()])
    passwd = PasswordField("passwd", validators=[DataRequired()])
    submit = SubmitField("提交")
    # recaptcha = RecaptchaField()

    def checkout_passwd(self):
        # print(self.data)
        email = self.data.get("email")
        passwd = self.data.get("passwd")
        user = User.query.filter_by(email=email).first()
        if check_password_hash(user.passwd, passwd):
            return True
        else:
            return False