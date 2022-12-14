import email
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


mypokemon = db.Table('mypokes',
    db.Column('caughtby_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('caught_id', db.Integer, db.ForeignKey('pokemon.id')),

)

battles = db.Table('battle',
    db.Column('battleWho_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('battler_id', db.Integer, db.ForeignKey('user.id')),

)

#create our models based off our ERD\
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique = True)
    password = db.Column(db.String(300), nullable=False)
    mypokes = db.relationship("Pokemon",
        # primaryjoin = (mypokemon.c.caughtby_id==id),
        # secondaryjoin = (mypokemon.c.caught_id==id),
        secondary = mypokemon,
        backref = db.backref('pokemon_owner', lazy = 'dynamic'),
        lazy = 'dynamic'
    )
    battle = db.relationship("User",
        primaryjoin = (battles.c.battleWho_id == id),
        secondaryjoin = (battles.c.battler_id == id),
        secondary = battles,
        backref = db.backref('battler', lazy = 'dynamic'),
        lazy = 'dynamic'
    )

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def updateAccount(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    def saveUpdates(self):
        db.session.commit()

    def catchPokemon(self, poke):
        self.mypokes.append(poke)
        db.session.commit()

    def releasePokemon(self,poke):
        self.mypokes.remove(poke)
        db.session.commit()

    def battles(self, user):
        self.battle.append(user)
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False, unique = True)
    attack = db.Column(db.String(100), nullable=False)
    defense = db.Column(db.String(150), nullable=False)
    hp = db.Column(db.String(300), nullable=False)
    ability= db.Column(db.String(100), nullable=False)
    imgurl = db.Column(db.String(300), nullable=False)


    def __init__(self, name, attack, defense, hp, ability,imgurl):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.ability = ability
        self.imgurl = imgurl


# class Battles