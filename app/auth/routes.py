from flask import Blueprint, render_template, request, redirect, url_for
from .forms import CreateUserForm, logInForm


# import login func
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

# import models
from app.models import User

auth = Blueprint('auth', __name__, template_folder='authtemplates')

from app.models import db


@auth.route('/login', methods = ['GET', 'POST'])
def logMeIn():
    form = logInForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data
            # query user based on username
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                else:
                    pass
            else:
                pass



    return render_template('login.html', form = form)

@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))


@auth.route('/signup', methods = ['GET', 'POST'])
def signMeUp():
    form = CreateUserForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            name = form.name.data
            email = form.email.data
            password = form.password.data

            print(username, name, email, password)

            # add user to database
            user = User(username, name, email, password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.logMeIn'))
        else:
            pass
    return render_template('signup.html', form = form)