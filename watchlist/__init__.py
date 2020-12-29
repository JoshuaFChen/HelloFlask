import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    return User.query.get(int(user_id))


@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return {'user': user}


from watchlist import views, errors, commands