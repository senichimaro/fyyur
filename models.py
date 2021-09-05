from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from datetime import datetime



#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# TODO: connect to a local postgresql database
# Migrations setup
migrate = Migrate(app, db)
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    genres = db.Column(db.ARRAY(db.String()), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=True)
    image_link = db.Column(db.String(500), nullable=True)
    website_link = db.Column(db.String(500), nullable=True)
    seeking_description = db.Column(db.String(), nullable=True)
    seeking_talent = db.Column(db.Boolean, default=False)
    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
        return f'''||| >>> Venue :
        ID-> {self.id}
        name -> {self.name}
        city -> {self.city}
        state -> {self.state}
        address -> {self.address}
        phone -> {self.phone}
        genres -> {self.genres}
        facebook_link -> {self.facebook_link}
        image_link -> {self.image_link}
        website_link -> {self.website_link}
        seeking_description -> {self.seeking_description}
        seeking_talent -> {self.seeking_talent}
        >'''


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String()), nullable=False)
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String())
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f'''||| >>> Artist :
        ID-> {self.id}
        name -> {self.name}
        city -> {self.city}
        state -> {self.state}
        phone -> {self.phone}
        genres -> {self.genres}
        facebook_link -> {self.facebook_link}
        image_link -> {self.image_link}
        website_link -> {self.website_link}
        seeking_venue -> {self.seeking_venue}
        seeking_description -> {self.seeking_description}
        >'''


class Show(db.Model):
    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
