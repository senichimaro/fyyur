import os
# My imports
from flask import Flask
from flask_moment import Moment

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_ECHO = True
# Connect to the database

# TODO IMPLEMENT DATABASE URL
APP_DATABASE_URI = os.getenv("APP_DATABASE_URI")
SQLALCHEMY_DATABASE_URI = APP_DATABASE_URI

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

SQLALCHEMY_TRACK_MODIFICATIONS = False
