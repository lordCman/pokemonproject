import requests
from flask import redirect, render_template,  Blueprint, request, url_for
import requests
from flask_login import login_required, current_user
from app.models import Pokemon, db, mypokemon, User


battle = Blueprint('battle', __name__, template_folder='battletemplates')


@battle.route('/battle')
def letsBattle():
    users = User.query.all()

    return render_template('battle.html', users=users)


@battle.route('/battle/<int:user_id>')
def battling(user_id):
    user = User.query.get(user_id)
    current_user.battles(user)
    return render_template('battling.html')