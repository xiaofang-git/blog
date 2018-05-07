from flask import Flask
from blog.views import blog
from blog.models import db

app = Flask(__name__)

app.config['RECAPTCHA_USE_SSL'] = True
# app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'  生成验证码用的
# app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
app.config['SECRET_KEY'] = "heh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0805@127.0.0.1:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_BINDS'] = {
    'users':        'mysql://root:0805@127.0.0.1:3306/blog',
    'appmeta':      'sqlite:////path/to/appmeta.db'
}

db.init_app(app)

app.register_blueprint(blog, url_prefix='/blog')

app.run(debug=True)
