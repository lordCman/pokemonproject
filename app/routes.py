import requests
from app import app
from flask import redirect, render_template,  Blueprint, request, url_for
import requests
from .models import User
from flask_login import login_required, current_user


from .forms import PokemonInfoForm, updateAcc

poke = Blueprint('poke', __name__, static_url_path='/pokemonInfo')

@app.route('/')
def home1():
    return render_template('home1.html')

@app.route('/pokemonInfo', methods = ['GET', 'POST'])
def pokemon():
    form = PokemonInfoForm()
    pokeDict = {}
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            pokemon_name = form.pokemon_name.data
            response = requests.get(f'http://pokeapi.co/api/v2/pokemon/{pokemon_name}')
            data = response.json()
            pokeDict = {}
            pokemon = data['name']
            pokeDict[pokemon] = {
                'name' : data['name'],
                'abilities' : data['abilities'][0]['ability']['name'],
                'base_exp' : data['base_experience'],
                'sprite' : data['sprites']['front_shiny'],
                'attack' : data['stats'][0]['base_stat'],
                'hp' : data['stats'][1]['base_stat'],
                'defense' : data['stats'][2]['base_stat']
                            } 
            print(pokeDict)
           

        else:
            return 'Validation failed'
            
            




    return render_template('pokemon.html', form = form, pokeDict = pokeDict, pokemon =pokemon)


@app.route('/account/')
@login_required
def acc():
    user = current_user.username
    return render_template('account.html', user=user)


app.route('/account/update', methods = ['GET', 'POST'])
def updateAccount(user):
    user = User.query.filter_by(username=current_user.id).first()
    form = updateAcc() 
    if current_user.id == user.id:
        if request.method=="POST":
            if user.validate():
                username = form.username.data
                name = form.name.data
                email = form.email.data

                user.updateAcc(username,name,email)
                user.saveUpdates()

                return redirect(url_for('acc', user =user, form = form))
        else:
            pass
    return render_template('updateAcc.html', user=user, form = form)

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