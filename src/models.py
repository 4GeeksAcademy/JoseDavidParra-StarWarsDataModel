import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, REAL
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250))
    password = Column(String(250))
    favorite_planets = relationship('FavoritePlanets',backref = 'user',lazy=True)
    favorite_characters = relationship('FavoriteCharacters',backref = 'user' ,lazy = True)
    favorite_starships = relationship('FavoriteStarships',backref = 'user' ,lazy = True)
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String)
    gravity = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    population = Column(Integer)
    usersPlanets = relationship('FavoritePlanets',backref = 'plantes',lazy=True)
    characters = relationship("Characters",backref = "planets",lazy =True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Integer)
    gender = Column(String)
    planet_id = Column(Integer,ForeignKey('planets.id'))
    usersCharacters = relationship('FavoriteCharacters',backref = 'characters',lazy=True)
    starships = relationship('Pilots',backref = 'characters' ,lazy = True)

class Starships(Base):
    __tablename__  = 'starships'
    id = Column(Integer,primary_key = True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String)
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(String)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String)
    hyperdrive_rating = Column(REAL)
    mglt = Column(Integer)
    starship_class = Column(String)
    usersStarships = relationship('FavoriteStarships',backref = 'starships',lazy=True)
    pilots = relationship('Pilots',backref = 'starships' ,lazy = True)

class Pilots(Base):
    __tablename__ = 'pilots'
    pilot_id = Column(Integer,ForeignKey('characters.id'),primary_key = True)
    starship_id = Column(Integer,ForeignKey('starships.id'),primary_key = True)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    user_id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    planet_id = Column(Integer,ForeignKey('planets.id'),primary_key = True)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    user_id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    character_id = Column(Integer,ForeignKey('characters.id'),primary_key = True)

class FavoriteStartchips(Base):
    __tablename__ = 'favorite_starships'
    user_id = Column(Integer,ForeignKey('user.id'),primary_key = True)
    startship_id = Column(Integer,ForeignKey('starships.id'),primary_key = True)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
