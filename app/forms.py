from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PokemonInfoForm(FlaskForm):
    pokemon_name = StringField('Pokemon', validators=[])
    submit = SubmitField()


    




# class updateAcc(FlaskForm):
#     username = StringField('Username', validators=[])
#     name = StringField('Name', validators=[])
#     email = StringField('Email', validators=[])
#     password = PasswordField('Password', validators=[])

class insertPokeForm(FlaskForm):
    name = StringField('Name')
    attack = StringField('Attack')
    defense = StringField('Defense')
    hp = StringField('Hp')
    ability = StringField('Ability')
    
    