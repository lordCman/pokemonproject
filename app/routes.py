import requests
from app import app
from flask import render_template,  Blueprint, request


from .forms import PokemonInfoForm

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
            
            




    return render_template('pokemon.html', form = form, pokeDict = pokeDict)