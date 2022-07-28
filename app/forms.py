from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class PokemonInfoForm(FlaskForm):
    pokemon_name = StringField('Pokemon', validators=[])
    submit = SubmitField()
    