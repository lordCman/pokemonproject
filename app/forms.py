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

    