import requests
from app import app
from flask import redirect, render_template,  Blueprint, request, url_for
import requests
from .models import User, Pokemon
from flask_login import login_required, current_user


from .forms import PokemonInfoForm

poke = Blueprint('poke', __name__, static_url_path='/pokemonInfo')

@app.route('/')
def home1():
    return render_template('home1.html')


@app.route('/account')
@login_required
def account():
    user = current_user
    return render_template('account.html', user=user)

# @app.route('/myPokemon')
# @login_required
# def getPoke():
#     return render_template('')




# app.route('/account/update', methods = ['GET', 'POST'])
# def updateAcc():
#     user = User.query.filter_by(username=current_user.id).first()
#     form = user.updateAccount()
#     if current_user.id == user.id:
#         if request.method=="POST":
#             if user.validate():
#                 username = form.username.data
#                 name = form.name.data
#                 email = form.email.data

#                 user.updateAcc(username,name,email)
#                 user.saveUpdates()

#                 return redirect(url_for('acc', user =user, form = form))
#         else:
#             pass
#     return render_template('updateAcc.html', user=user, form = form)

# @ig.route('/posts/update/<int:post_id>', methods=["GET", "POST"])
# def updatePost(post_id):
#     form = PostForm()
#     # post = Post.query.get(post_id)
#     post = Post.query.filter_by(id=post_id).first()
#     if current_user.id != post.user_id:
#         flash('You are not allowed to update another user\'s posts.', 'danger')
#         return redirect(url_for('ig.getSinglePost', post_id=post_id))
#     if request.method=="POST":
#         if form.validate():
#             title = form.title.data
#             img_url = form.img_url.data
#             caption = form.caption.data

#             post.updatePostInfo(title,img_url,caption)
#             post.saveUpdates()
#             flash('Successfully updated post.', 'success')
#             return redirect(url_for('ig.getSinglePost', post_id=post_id))
#         else:
#             flash('Invalid form. Please fill out the form correctly.', 'danger')
#     return render_template('updatepost.html', form=form,  post=post)


# app.route('/account/update', methods = ['GET', 'POST'])
# def update():
#     return render_template('updateAcc.html')

