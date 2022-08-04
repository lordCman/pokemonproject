
import requests
from flask import redirect, render_template,  Blueprint, request, url_for
import requests
from flask_login import login_required, current_user
from app.models import Pokemon, db, mypokemon, User
from .forms import PokemonInfoForm



poke = Blueprint('poke', __name__, template_folder='poketemplates')



@poke.route('/pokemonInfo', methods = ['GET', 'POST'])
def pokemon():
    form = PokemonInfoForm()
    pokeDict = {}
    p_set = set()
    pokemon_name = form.pokemon_name.data
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
            check = Pokemon.query.filter_by(name=pokemon_name).first()
            if check:
                pass
            else:
                poke = Pokemon(pokemon_name, pokeDict['attack'], pokeDict['defense'], pokeDict['hp'], pokeDict['abilities'], pokeDict['sprite'])
                db.session.add(poke)
                db.session.commit()
                 
            

            p1 = current_user.mypokes               
            p_set = {p.name for p in p1}
            print(p_set)
            flag = False
            if pokeDict['name'] in p_set:
                flag = True
            return render_template('pokemon.html', form = form, pokeDict=pokeDict, flag =flag)



    return render_template('pokemon.html', form = form, pokeDict=pokeDict)
    
@poke.route('/myPokemon')
@login_required
def getPoke():
    pokemon = current_user.mypokes.all()
    print(pokemon[0].name)
    return render_template('myPoke.html',pokemon = pokemon)


@poke.route('/catchPoke/<pokemon>')
@login_required
def catchPoke(pokemon):
    poke = Pokemon.query.filter_by(name = pokemon).first()
    current_user.catchPokemon(poke)
    return redirect(url_for('poke.getPoke'))

@poke.route('/releasePoke/<pokemon>')
@login_required
def releasePoke(pokemon):
    poke = Pokemon.query.filter_by(name = pokemon).first()
    current_user.releasePokemon(poke)
    return redirect(url_for('poke.getPoke'))


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