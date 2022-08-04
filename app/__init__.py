from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_migrate import Migrate

from.pokemon.routes import poke
from .battle.routes import battle

# import blueprints
from .auth.routes import auth
from .models import User, Pokemon 

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth)

app.register_blueprint(poke)

app.register_blueprint(battle)

app.config.from_object(Config)


# initialize our database to work w our app
from .models import db


db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)


from . import routes
from . import models