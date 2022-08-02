from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class PokemonInfoForm(FlaskForm):
    pokemon_name = StringField('Pokemon', validators=[])
    submit = SubmitField()