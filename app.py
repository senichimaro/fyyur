#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
# My imports
from flask_migrate import Migrate
import sys
import os
from models import *



#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():

  venues = Venue.query.order_by('id').all()
  db_clean = []
  for v in venues:
      v_item = {}
      v_item['city'] = v.city
      v_item['state'] = v.state
      v_venues = []
      for place in venues:
          if v.city == place.city and v.state == place.state:
              v_venues.append({ "id":place.id,"name":place.name })
      v_item['venues'] = v_venues
      db_clean.append(v_item)

  return render_template('pages/venues.html', areas=db_clean);

@app.route('/venues/search', methods=['POST'])
def search_venues():

  term = request.form.get('search_term', '')
  search = Venue.query.filter(Venue.name.ilike(f"%{term}%"))

  response={
    "count": search.count(),
    "data": search
  }
  return render_template('pages/search_venues.html', results=response, search_term=term)

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):

  venue = Venue.query.get(venue_id)
  return render_template('pages/show_venue.html', venue=venue)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():

  error = False
  try:
      form_data = {}
      form3 = VenueForm(meta={'csrf':False})
      form_data['name'] = form3.name.data
      form_data['city'] = form3.city.data
      form_data['state'] = form3.state.data
      form_data['address'] = form3.address.data
      form_data['phone'] = form3.phone.data
      form_data['genres'] = form3.genres.data
      form_data['facebook_link'] = form3.facebook_link.data
      form_data['image_link'] = form3.image_link.data
      form_data['website_link'] = form3.website_link.data
      form_data['seeking_description'] = form3.seeking_description.data
      form_data['seeking_talent'] = form3.seeking_talent.data
      venue = Venue(
          name=form_data['name'],
          city=form_data['city'],
          state=form_data['state'],
          address=form_data['address'],
          phone=form_data['phone'],
          genres=form_data['genres'],
          facebook_link=form_data['facebook_link'],
          image_link=form_data['image_link'],
          website_link=form_data['website_link'],
          seeking_description=form_data['seeking_description'],
          seeking_talent=form_data['seeking_talent'],
      )
      db.session.add(venue)
      db.session.commit()
  except:
      error = True
      flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed')
      db.session.rollback()
      print(sys.exc_info())
  finally:
      db.session.close()
  if error:
      abort(400)
  else:
      # on successful db insert, flash success
      flash('Venue ' + request.form['name'] + ' was successfully listed!')
      return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return None

#  Update Venue
#  ----------------------------------------------------------------
@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
    form = VenueForm()
    venue = Venue.query.get(venue_id)
    return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):

  error = False
  try:
      venue = Venue.query.get(venue_id)
      form3 = VenueForm()

      venue.name = form3.name.data
      venue.city = form3.city.data
      venue.state = form3.state.data
      venue.address = form3.address.data
      venue.phone = form3.phone.data
      venue.genres = form3.genres.data
      venue.facebook_link = form3.facebook_link.data
      venue.image_link = form3.image_link.data
      venue.website_link = form3.website_link.data
      venue.seeking_description = form3.seeking_description.data
      venue.seeking_talent = form3.seeking_talent.data

      db.session.commit()
  except:
      error = True
      flash('An error occurred. Venue ' + request.form['name'] + ' could not be edited')
      db.session.rollback()
      print(sys.exc_info())
  finally:
      db.session.close()
  if error:
      abort(400)
  else:
      # on successful db insert, flash success
      flash('Venue ' + request.form['name'] + ' was successfully edited!')
      return redirect(url_for('show_venue', venue_id=venue_id))

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():

    artists = Artist.query.all()
    return render_template('pages/artists.html', artists=artists)

@app.route('/artists/search', methods=['POST'])
def search_artists():

    term = request.form.get('search_term', '')
    search = Artist.query.filter(Artist.name.ilike(f"%{term}%"))
    response={
        "count": search.count(),
        "data": search
    }
    return render_template('pages/search_artists.html', results=response, search_term=term)

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):

  artist = Artist.query.get(artist_id)
  return render_template('pages/show_artist.html', artist=artist)

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():

  error = False
  try:
      formArtist = ArtistForm()
      theArtist = Artist(
          name=formArtist.name.data,
          city=formArtist.city.data,
          state=formArtist.state.data,
          phone=formArtist.phone.data,
          genres=formArtist.genres.data,
          facebook_link=formArtist.facebook_link.data,
          image_link=formArtist.image_link.data,
          website_link=formArtist.website_link.data,
          seeking_venue=formArtist.seeking_venue.data,
          seeking_description=formArtist.seeking_description.data
      )
      db.session.add(theArtist)
      db.session.commit()
  except:
      error = True
      flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
      db.session.rollback()
      print(sys.exc_info())
  finally:
      db.session.close()
  if error:
      abort(400)
  else:
      # on successful db insert, flash success
      flash('Artist ' + request.form['name'] + ' was successfully listed!')
      return render_template('pages/home.html')

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    form = ArtistForm()
    artist = Artist.query.get(artist_id)
    return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):

  error = False
  try:
      artist = Artist.query.get(artist_id)
      formArtist = ArtistForm()
      artist.name = formArtist.name.data
      artist.city = formArtist.city.data
      artist.state = formArtist.state.data
      artist.phone = formArtist.phone.data
      artist.genres = formArtist.genres.data
      artist.facebook_link = formArtist.facebook_link.data
      artist.image_link = formArtist.image_link.data
      artist.website_link = formArtist.website_link.data
      artist.seeking_venue = formArtist.seeking_venue.data
      artist.seeking_description = formArtist.seeking_description.data

      db.session.commit()
  except:
      error = True
      flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
      db.session.rollback()
      print(sys.exc_info())
  finally:
      db.session.close()
  if error:
      abort(400)
  else:
      # on successful db insert, flash success
      flash('Artist ' + request.form['name'] + ' was successfully listed!')
      return redirect(url_for('show_artist', artist_id=artist_id))

#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  shows = Show.query.all()
  return render_template('pages/shows.html', shows=shows)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
    # called to create new shows in the db, upon submitting new show listing form
    # TODO: insert form data as a new Show record in the db, instead

    error = False
    try:
        formShow = ShowForm()
        theShow = Show(
            venue_id=formShow.venue_id.data,
            artist_id=formShow.artist_id.data,
            start_time=formShow.start_time.data,
        )
        db.session.add(theShow)
        db.session.commit()
    except:
        error = True
        flash('An error occurred. Show could not be listed.')
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error:
            abort(400)
        else:
            # on successful db insert, flash success
            flash('Show was successfully listed!')
            return render_template('pages/home.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
