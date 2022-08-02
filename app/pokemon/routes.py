from unicodedata import name
import requests
from flask import redirect, render_template,  Blueprint, request, url_for
import requests
from flask_login import login_required, current_user
from app.models import Pokemon, db
from .forms import PokemonInfoForm
from psycopg2 import IntegrityError



poke = Blueprint('poke', __name__, template_folder='poketemplates')



@poke.route('/pokemonInfo', methods = ['GET', 'POST'])
def pokemon():
    form = PokemonInfoForm()
    pokeDict = {}
    pokemon_name = form.pokemon_name.data
    try:
        if request.method == "POST":
            pokemon_name = form.pokemon_name.data
            print('POST request made')
            if form.validate():
                
                response = requests.get(f'http://pokeapi.co/api/v2/pokemon/{pokemon_name}')
                data = response.json()
        
                pokeDict = {
                    'name' : data['name'],
                    'abilities' : data['abilities'][0]['ability']['name'],
                    'base_exp' : data['base_experience'],
                    'sprite' : data['sprites']['front_shiny'],
                    'attack' : data['stats'][0]['base_stat'],
                    'hp' : data['stats'][1]['base_stat'],
                    'defense' : data['stats'][2]['base_stat']
                                } 
                poke = Pokemon(pokemon_name, pokeDict['attack'], pokeDict['defense'], pokeDict['hp'], pokeDict['abilities'])
                db.session.add(poke)
                db.session.commit()
                return render_template('pokemon.html', form = form, pokeDict=pokeDict)

    except:
        IntegrityError
        db.session.rollback()
        return render_template('pokemon.html', form = form, pokeDict=pokeDict)

    return render_template('pokemon.html', form = form, pokeDict=pokeDict)
    
@poke.route('/myPokemon')
@login_required
def getPoke():
    return render_template('myPoke.html')


# from app import db
# import json
# import requests

# db = db.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="pokemon",
# )
# pokemon = db.Pokemon()

# for i in range(1,150):
#     url = 'https://pokeapi.co/api/v2/pokemon/'+ str(i)
#     r = requests.get(url)
#     pokemontable = json.loads(r.text)

# pokemonlist = []
# for i in pokemontable:
#   pokemon = {
#   'id': pokemontable['id'],
#   'name': pokemontable['name'],
#   'weight': pokemontable['weight'],
#   'height': pokemontable['height']
#   }


#   pokemonlist.append(pokemon)

# cursor.execute("CREATE TABLE pokemon (id INT(22), name VARCHAR(255), weight INT(22), height INT(22))")

# sql = """INSERT INTO pokemon 
# (id, name, weight, height) 
# VALUES (%(id)s, %(name)s, %(weight)s, %(height)s)"""
# for pokemon in pokemonlist:
#     cursor.execute(sql, pokemon)

# db.commit()
# db.close()